#!/usr/bin/env python3
import sys
import json
import time
import requests
import re
try:
    from .credentials import Credentials
except:
    from credentials import Credentials

from pprint import pprint

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.force-ssl"]

VERSION = "0.3.2"
PYTHONIOENCODING = "UTF-8"
debug = 0
data = {}
# store data[chat id][user id] = {
# 'msg': 'asd',
# 'date': datetime
# }

prefix = '!'

class YTChat:
    def __init__(self, cb):
        self.cb = cb
        self.credentials = Credentials()
        self.token_str = self.credentials.read()
        self.liveChatID = self.get_livechat_id()
        self.stopped = False
        if not self.liveChatID:
            print("[] No livestream found :(")
        else:
            print("Live Chat ID", self.liveChatID)

    def handle_msg(self, msg):
        # pprint(msg)
        message = re.search(r"\'([A-Za-z0-9_]+)\'", msg["snippet"]["textMessageDetails"]["messageText"])
        author = re.search(r"\'([A-Za-z0-9_]+)\'", msg["authorDetails"]["displayName"])
        if msg["snippet"]["type"] != "textMessageEvent":
            print("non text message event")
            return
        self.cb(author + message)

    def main(self):
        nextPageToken = ''
        token_str = ''
        while not self.stopped:
            # Make sure access token is valid before request
            # credentials.read() should refresh the token automatically
            if self.credentials.expired() or token_str == '':
                token_str = self.credentials.read()

            payload = {'liveChatId': self.liveChatID,
                       'part': 'snippet,authorDetails',
                       'pageToken': nextPageToken}
            url = 'https://content.googleapis.com/youtube/v3/liveChat/messages'
            headers = {"Authorization": "Bearer " + token_str}
            r = requests.get(url, headers=headers, params=payload)

            if (r.status_code == 200):
                resp = r.json()
                nextPageToken = resp["nextPageToken"]
                msgs = resp["items"]
                for msg in msgs:
                    self.handle_msg(msg)

                delay = resp['pollingIntervalMillis']/1000
            elif (r.status_code == 401):  # Unauthorized
                delay = 10
                if not self.credentials.expired:
                    print("Error: Unauthorized. waiting 30 seconds...")
                    if (debug >= 1):
                        resp = r.json()
                        print(json.dumps(resp, indent=4, sort_keys=True))
                    delay = 30
            else:
                print("Unrecognized error:\n")
                resp = r.json()
                print(json.dumps(resp, indent=4, sort_keys=True))
                delay = 30
                delay = 3  #FIXME testing

            time.sleep(delay)

    def get_livechat_id(self):
        token_str = self.credentials.read()
        payload = {'broadcastStatus': 'active',
                   'broadcastType': 'all',
                   'part': 'id,snippet,contentDetails'
                   }
        headers = {"Authorization": "Bearer " + token_str}
        url = 'https://content.googleapis.com/youtube/v3/liveBroadcasts'
        r = requests.get(url, headers=headers, params=payload)
        if r.status_code == 200:
            resp = r.json()
            if len(resp["items"]) == 0:
                return False
            else:
                # Should only be 1 item unless YT adds multiple livestreams
                # then we'll assume it's the first for now
                print("Live events:", len(resp["items"]))
                # pprint(resp)
                print("*" * 50)
                streamMeta = resp["items"][0]["snippet"]
                liveChatID = streamMeta["liveChatId"]
                return liveChatID
        else:
            print("Unrecognized error:\n")
            resp = r.json()
            print(json.dumps(resp, indent=4, sort_keys=True))

    def send_message(liveChatID,message,author,prefix):
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secrets.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)
        liveChatId = print(f'"{liveChatID}"')

        # NEW COMMANDS
        if message == prefix + "command":
            newmessage = "This is a test of the command system."

        request = youtube.liveChatMessages().insert(
            part="snippet",
            body={
              "snippet": {
                "liveChatId": liveChatId,
                "textMessageDetails": {
                  "messageText": newmessage
                },
                "type": "textMessageEvent"
              }
            }
        )
        response = request.execute()
        print(response)

if __name__ == '__main__':
    yt = YTChat(pprint)
    yt.main()
  