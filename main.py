import tweepy
import time
from Modules.NDaysOfCode import NDaysOfCode
import os
FREQUENCY = int(os.getenv('FREQUENCY'))
API_Key = os.getenv('API_KEY')
API_Key_Secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
acces_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
# auth = tweepy.OAuth2UserHandler()

auth = tweepy.OAuthHandler(API_Key, API_Key_Secret,access_token, acces_token_secret)
api = tweepy.API(auth)

p1 = NDaysOfCode(api,100)

while(True):
    p1.quote_retweet()
    print("Sleeping for " + str(FREQUENCY) + " seconds")
    time.sleep(FREQUENCY)