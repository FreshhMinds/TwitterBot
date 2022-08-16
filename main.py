import tweepy
import time
from private import *
from Modules.NDaysOfCode import NDaysOfCode
# auth = tweepy.OAuth2UserHandler()

auth = tweepy.OAuthHandler(API_Key, API_Key_Secret,access_token, acces_token_secret)
api = tweepy.API(auth)

p1 = NDaysOfCode(api,100)

while(True):
    p1.quote_retweet()
    print("Iterating..")
    time.sleep(60)