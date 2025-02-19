from google.oauth2.credentials import Credentials
from google_auth_httplib2 import AuthorizedHttp
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request  # Import Request
import os.path
import pickle
import logging


def authenticate_google(scopes, client_secret_file, token_file='token.pickle'):
    creds = None
    if os.path.exists(token_file):
        try:
            with open(token_file, 'rb') as token:
                creds = pickle.load(token)
        except Exception as e:
            logging.error(f"Error loading token file: {e}")
            os.remove(token_file)  # Delete the corrupted token file
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                logging.exception("Error refreshing token:")
                # Delete the token file and re-authenticate
                os.remove(token_file)
                creds = None # Set creds to None to force re-authentication.
                return authenticate_google(scopes,client_secret_file,token_file) #Recursive call
        if not creds: # Re-authentication required
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_file, scopes)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                logging.exception("Error during authentication flow:")
                return None  # Return None on authentication failure

        try:
            with open(token_file, 'wb') as token:
                pickle.dump(creds, token)
        except Exception as e:
            logging.error(f"Error saving token file: {e}")

    return creds