#!/usr/bin/env python3
import json
import time
import requests
try:
    from .credentials import Credentials
except:
    from credentials import Credentials

from pprint import pprint

#import re
#import google_auth_oauthlib.flow
#import googleapiclient.discovery
#import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.force-ssl"]

VERSION = "0.3.2"
PYTHONIOENCODING = "UTF-8"
debug = 0
data = {}
# store data[chat id][user id] = {
# 'msg': 'asd',
# 'date': datetime
# }

class YTChat:
    def __init__(self, cb):
        self.cb = cb
        self.credentials = Credentials()
        self.token_str = self.credentials.read()
        self.liveChatID = self.get_livechat_id()
        self.stopped = False
        self.prefix = '!'
        if not self.liveChatID:
            print("[] No livestream found :(")
        else:
            print("Live Chat ID", self.liveChatID)

    def handle_msg(self, msg):
        # pprint(msg)
        self.message = msg["snippet"]["textMessageDetails"]["messageText"]
        self.author = msg["authorDetails"]["displayName"]
        comb = str(self.author + ": " + self.message)
        if msg["snippet"]["type"] != "textMessageEvent":
            print("non text message event")
            return
        self.cb(comb)
        if self.message.startswith(self.prefix):
          if self.message == str(self.prefix + "command"):
            response = "This is a test of the command system."
            self.send_message(response)

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

    def send_message(self,response=None):
        token_str = ''
        while not self.stopped:
            # Make sure access token is valid before request
            # credentials.read() should refresh the token automatically
            if self.credentials.expired() or token_str == '':
                token_str = self.credentials.read()

            payload1 = {"snippet": {"textMessageDetails": {"messageText": response}} ,"type": "textMessageEvent","liveChatId": self.liveChatID}
            result = json.dumps(payload1)
            payload = print(str(result))
            url = 'https://content.googleapis.com/youtube/v3/liveChat/messages'
            headers1 = {'Authorization': 'Bearer ' + token_str, 'Accept': 'application/json', 'Content-Type': 'application/json'}
            result2 = json.dumps(headers1)
            headers = print(str(result2))
                        
            r = requests.post(url, headers=headers, params=payload)

            if (r.status_code == 200):
              resp = r.json()
              send = resp["items"]
              if response != "None":
                print(send)
              self.stopped = True

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

            time.sleep(delay)
if __name__ == '__main__':
    yt = YTChat(pprint)
    yt.main()
  