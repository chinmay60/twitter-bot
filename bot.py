import tweepy
from time import sleep
from key import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

count = 1

for tweet in tweepy.Cursor(api.search, q='#funfact').items(1): #change #funfact to any other hashtag you want 
    
    try:

        tweet.retweet()
        print("count = "+count)
        sleep = (3600)
    
    except tweepy.TweepError as error:

        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break