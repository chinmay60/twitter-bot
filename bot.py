import tweepy
from time import sleep
# insert keys here 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
count = int(10000)


for tweet in tweepy.Cursor(api.search, q='#funfact').items(count):
    try:
        #print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'retweet attempt..')

        tweet.retweet()
        #print('successful')
        count = int(10000)
        sleep(3600) #1hr

    except tweepy.TweepError as error:
        print('\nError! Retweet failed!.')
        print(error.reason)

    except StopIteration:
        break
