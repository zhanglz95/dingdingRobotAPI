import requests
import time
import hmac
import hashlib
import urllib
import base64

class DingRobot:
    def __init__(self, url, secret):
        self.timestamp, self.sign = self.getSign(secret)
        self.url = url + f'&timestamp={self.timestamp}&sign={self.sign}'

    def sendText(self, message, at=[], isAtAll=False):
        headers= {
            'Content-Type' : 'application/json'
        }

        json = {
            "msgtype": "text",
            "text": {
                "content": message
            },
            "at": {
                "atMobiles": at,
                "isAtAll": isAtAll
            }
        }        

        resp = requests.post(url=self.url, headers=headers, json=json)
        print(resp.text)
    
    def sendLink(self, text, title, picUrl="", msgUrl=""):
        headers= {
            'Content-Type' : 'application/json'
        }

        json = {
            "msgtype": "link",
            "link":{
                "text": text,
                "title": title,
                "picUrl": picUrl,
                "messageUrl": msgUrl
            }
        }

        resp = requests.post(url=self.url, headers=headers, json=json)
        print(resp.text)
    
    def sendMd(self, title, md, isAtAll=False):
        headers= {
            'Content-Type' : 'application/json'
        }
        json = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": md
            },
            "at": {
                "isAtAll": isAtAll
            }
        }
        resp = requests.post(url=self.url, headers=headers, json=json)
        print(resp.text)
    

    @staticmethod
    def getSign(secret):
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = f'{timestamp}\n{secret}'
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign