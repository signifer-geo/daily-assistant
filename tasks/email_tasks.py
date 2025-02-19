from utils.auth import authenticate_google
from config import GMAIL_SCOPES, GOOGLE_CLIENT_SECRET_FILE
from googleapiclient.discovery import build
import logging
import base64
from email.message import EmailMessage

def get_unread_email_summaries():
    try:
        creds = authenticate_google(GMAIL_SCOPES, GOOGLE_CLIENT_SECRET_FILE, 'token_gmail.pickle')
        service = build('gmail', 'v1', credentials=creds)

        results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        messages = results.get('messages', [])

        summaries = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
            # Extract headers
            headers = msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'No Sender')

            # Extract the body, handling different MIME types.
            body = ""
            if 'parts' in msg['payload']:
                parts = msg['payload']['parts']
                # Find the text/plain part, or text/html if plain is not available
                for part in parts:
                    if part['mimeType'] == 'text/plain':
                        data = part['body']['data']
                        body = base64.urlsafe_b64decode(data).decode()
                        break
                    elif part['mimeType'] == 'text/html' and not body:
                        data = part['body']['data']
                        body = base64.urlsafe_b64decode(data).decode()
            elif msg['payload']['mimeType'] in ['text/plain', 'text/html']:
                data = msg['payload']['body']['data']
                body = base64.urlsafe_b64decode(data).decode()

            summaries.append(f"From: {sender}\nSubject: {subject}\nBody Snippet: {body[:200]}...\n---")  # Show a snippet

        return summaries

    except Exception as e:
        logging.exception("Error getting email summaries:")
        return []
