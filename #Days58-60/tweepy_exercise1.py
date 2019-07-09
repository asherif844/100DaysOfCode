from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt 
%matplotlib inline 


consumerKey = "tIgpFmAJLons76Hp9u6801MMd"
consumerSecret = "ZhI1KeF50j3vSG8Gk7t03kJAjRyBSQa5FYBD2zpUYe6fdDTEtz"
accessToken = "33629020-QqJAsjyI5VsZpArTQ0pBPebnAoh29A5jT6nVOg20f"
accessTokenSecret = "xxKyD9v7iOhv70YOgwUZQENzXrouSgKSXLm3R1e9X515u"

def percentage(part, whole):
    return 100 * float(part)/float(whole)


percentage(5,100)


auth = tweepy.OAuthHandler(consumer_key = consumerKey, 
                            consumer_secret = consumerSecret)

auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

# searchTerm = input("Enter keyword/hashtag to search about: ")
searchTerm = 'trump'
# noOfSearchTerms = int(input("Enter how many tweets to analyze: "))
noOfSearchTerms = 100
tweets = tweepy.Cursor(api.search, q = searchTerm).items(noOfSearchTerms)



positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity +=analysis.sentiment.polarity
    if analysis.sentiment.polarity ==0:
        neutral +=1
    elif analysis.sentiment.polarity <0:
        negative +=1
    else:
        positive +=1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral  = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral  = format(neutral, '.2f')


ttl = f'How people are reacting on {searchTerm} by analyzing {noOfSearchTerms} Tweets.'

if polarity == 0:
    print('neutral')
elif polarity <0:
    print('negative')
else:
    print('positive')

labels = [f'Positive: {positive}%, Negative: {negative}%, Neutral: {neutral}%']
sizes = [positive, negative, neutral]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title(ttl)
plt.axis('equal')
plt.tight_layout()
plt.show()
