import os.path
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def cal_requests():
    CALENDAR_SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
                       'https://www.googleapis.com/auth/calendar',
                       'https://www.googleapis.com/auth/calendar.events.readonly',
                       'https://www.googleapis.com/auth/calendar.events']
    all_events = []
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file('calendar_resources/client_secret.json', CALENDAR_SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    all_events.append(events)
    print(all_events)
    output = []
    for event in all_events:
        newstr = ""
        newstr += event["summary"] + ", updated: " + event["updated"] + ", "
        for i in event["items"]:
            newstr += i["summary"] + ", link: " + i["htmlLink"]
        output.append(newstr)
    return output
