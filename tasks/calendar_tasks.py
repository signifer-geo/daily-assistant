from utils.auth import authenticate_google
from config import CALENDAR_SCOPES, GOOGLE_CLIENT_SECRET_FILE
from googleapiclient.discovery import build
import datetime
import logging

def get_todays_events():
    try:
        creds = authenticate_google(CALENDAR_SCOPES, GOOGLE_CLIENT_SECRET_FILE, 'token_calendar.pickle')
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC
        events_result = service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        event_list = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list.append(f"{start} - {event['summary']}")
        return event_list

    except Exception as e:
        logging.exception("Error getting calendar events:")
        return [] # Return an empty list on error