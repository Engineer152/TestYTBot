import sys
import os.path
import httplib2
from oauth2client import client

#python3 ~/DPGLive/Live1/credentials.py

class Credentials:
    credentials = {}

    def expired(self):
        return self.credentials.access_token_expired

    def read(self,num):
        #if not os.path.isfile("OAuthCredentials.json"):
        #    print("Auth first")
        #    sys.exit(1)
        # LIST OF MULTIPLE STREAM CREDENTIALS
        if num == 1:
          credentialsFile = open("./Credentials/DPGBot1/OAuthCredentials.json", "r")
        if num == 2:
          credentialsFile = open("./Credentials/DPGBot2/OAuthCredentials.json", "r")
        if num == 3:
          credentialsFile = open("./Credentials/DPGBot3/OAuthCredentials.json", "r")
        if num == 4:
          credentialsFile = open("./Credentials/DPGBot4/OAuthCredentials.json", "r")
        # MAIN BOT CREDENTIALS
        elif num == 10: 
          credentialsFile = open("./Credentials/MainDPGBot/dpgbotOAuthCredentials.json", "r")
        credentialsJSON = credentialsFile.read()

        self.credentials = client.OAuth2Credentials.from_json(credentialsJSON)

        token_obj = self.credentials.get_access_token()
        token_str = str(token_obj.access_token)
        return token_str
        
    def auth(self):
        if os.path.isfile("OAuthCredentials.json"):
            print("Trying to auth but OAuthCredentials.json exists")
            return
        flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope=['https://www.googleapis.com/auth/youtube.force-ssl','https://www.googleapis.com/auth/youtube.readonly','https://www.googleapis.com/auth/youtube'],
            redirect_uri='https://dpgbot.appspot.com/oauth2callback')

        auth_uri = flow.step1_get_authorize_url()
        print(auth_uri)

        print("Open the shown link")
        auth_code = input('Enter the auth code: ')

        self.credentials = flow.step2_exchange(auth_code)
        self.credentials.authorize(httplib2.Http())

        outFile = open("OAuthCredentials.json", "w")
        outFile.write(str(self.credentials.to_json()))
        outFile.close()


if __name__ == '__main__':
    c = Credentials()
    c.auth()
