import os
import tweepy
from datetime import date, timedelta
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
# print(user.name)
# print(user.location)
print("Welcome\t\t: " + user.name)
print("Your location\t: " + user.location)
print("=====================================")

#Mencari kata
for status in tweepy.Cursor(api.search, q='cerita horror', src='recent_search_click', f='live', lang='id').items(50):
    try:
        print('============================================')
        print('\nTweet by: @' + status.user.screen_name)
        print(status.text)
        print(status.created_at)
        print(status.source)
        status.retweet()
        status.favorite()
        print('Done !!!')
        print('============================================')
        print('\n')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
