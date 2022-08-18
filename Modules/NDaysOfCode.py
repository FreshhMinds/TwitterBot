import re
from tweepy.errors import Forbidden
from Modules.db import get_retweets_from_db, insert_retweet_to_db
class NDaysOfCode:
    def __init__(self, api, days=100):
        self.api = api
        self.hashtags = ['100daysofcode', 'freshhmindsfolks']
        self.noOfDays = days
        self.history = get_retweets_from_db()
    def get_mensions(self):
        return self.api.mentions_timeline()
    def filter_tweets(self, tweets):

        for tweet in tweets:
            tweet = self.api.get_status(tweet.id, tweet_mode='extended')
            h = []
            for hashtag in self.hashtags:
                for tweet_hashtag in tweet.entities['hashtags']:
                    if hashtag == tweet_hashtag['text'].lower():
                        h.append(True)
                        break
                    else:
                        pass
                else:
                    h.append(False)
            if all(h):
                yield tweet
                        
                    
            # if '#100daysofcode' in tweet.full_text.lower() and 'freshhmindsfolks' in tweet.hashtags.lower():
            #     t.append(tweet)
        # print(t)
    def get_tweet_url(self, tweet):
        return 'https://twitter.com/%s/status/%s' % (tweet.user.screen_name, tweet.id)
    def get_day_number(self, tweet):
        lower_text = tweet.full_text.lower()
        day_numbers = re.findall(r'\d+', lower_text)
        for day_number in day_numbers:
            start = len(lower_text[:lower_text.find(day_number)]) - 4
            day_text = lower_text[start:lower_text.find(day_number)]
            if day_text == 'day ':
                return day_number
            else:
                pass
        return None
    def quote_retweet(self):
        tweets = list(self.filter_tweets(self.get_mensions()))
        for tweet in list(self.filter_tweets(self.get_mensions())):
            if self.get_day_number(tweet) != None:
                try:
                    if str(tweet.id) not in self.history:
                        self.api.update_status('Day %s of #freshhmindsfolks! Check out the latest tweet by %s at %s' % (self.get_day_number(tweet), tweet.author.name ,self.get_tweet_url(tweet)))
                        self.history.append(str(tweet.id))
                        insert_retweet_to_db(str(tweet.id))
                        print('Day %s of #freshhmindsfolks! Check out the latest tweet by %s at %s' % (self.get_day_number(tweet), tweet.author.name ,self.get_tweet_url(tweet)))
                        print('tweeted')
                    else:
                        print('already tweeted')
                except Forbidden:
                    print('Forbidden')
            else:
                pass