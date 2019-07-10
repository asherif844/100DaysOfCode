import os
import re
from collections import Counter, namedtuple

import numpy as np
import tweepy

consumerKey = "tIgpFmAJLons76Hp9u6801MMd"
consumerSecret = "ZhI1KeF50j3vSG8Gk7t03kJAjRyBSQa5FYBD2zpUYe6fdDTEtz"
accessToken = "33629020-QqJAsjyI5VsZpArTQ0pBPebnAoh29A5jT6nVOg20f"
accessTokenSecret = "xxKyD9v7iOhv70YOgwUZQENzXrouSgKSXLm3R1e9X515u"

twitterAccount = 'theahmedsherif'

Tweet = namedtuple('Tweet', 'id text created likes rts')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name = twitterAccount, exclude_replies = False, include_rts = True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)

tweets = list(get_tweets())

tweets[0]