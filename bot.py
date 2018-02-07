import tweepy
from time import sleep

consumer_key = 'ERTTYHTAx6P91fLzrTTvabh1I'
consumer_secret = 'PAiFjEEM2EzD7AFiiOij3viOZeVK884zuixqc4oZvgRigHsNKE'
access_token = '961295881982033920-fJYqNvx0IYDTcz4OodNuJrcT93pJANp'
access_token_secret = '19ppgAk9k9jbEJsTBMbBFr97pxM6nYirJC7vQcsX0CBFR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
count = int(10000)


for tweet in tweepy.Cursor(api.search, q='#funfact').items(count):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')
        count = int(10000)
        sleep(1)

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
