
import praw
import datetime as dt
import RedditPy.sendemail
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, render_template, url_for, json


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']
    
"""Shows basic usage of the Gmail API.
Lists the user's Gmail labels.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/content", "credentials2.json")
        flow = InstalledAppFlow.from_client_secrets_file(
            json_url, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

# Call the Gmail API
results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name'])


def hwswapper(item):
    reddit = praw.Reddit(client_id='IFugSTcSnsbizw', \
                     client_secret='3wVkiQFjmbbUsCnVCcn371sSwQY', \
                     user_agent='hardwareswapcheck', \
                     username='timbombadil9', \
                     password='')
    hwswap = reddit.subreddit('hardwareswap')
    testsub = ''
    for submission in hwswap.search('{} flair:selling'.format(item), sort ='new', time_filter= 'week'):
        testsub += submission.title + '\n'
        print(submission.title)



    new_message = RedditPy.sendemail.create_message('me', 'devin.tark@gmail.com', 'new sale', testsub)

    RedditPy.sendemail.send_message(service, 'me' , new_message)