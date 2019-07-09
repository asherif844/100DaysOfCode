from textblob import TextBlob
from statistics import mean

emails = ["Everything is awesome, everything is cool when your part of a team",
          "Everything is awesome, when you're living out a dream",
          "Everything is better when we stick together",
          "Some have said you and I are gonna win forever?",
          "Lets party forever",
          "We're the same unlike you, you're like me we're all working in harmony",
          "Everything is awesome, everything is cool when your part of a team",
          "Everything is awesome, when you're living out a dream",
          "Woo! 3, 2, 1, go!",
          "Have you heard the news? Everyone's talkin'",
          "Life is good 'cause everything awesome",
          "Lost my job, there's a new opportunity",
          "More free time for my awesome community",
          "I feel more awesome than an awesome possum",
          "Dip my body in chocolate frostin'",
          "Three years later wash off the frostin'",
          "Smellin' like…"]

emails2 = []




# sentiment = []
# polarity = []
# for i in emails:
#     i = i.split('.')
#     for j in i:
#         sent = TextBlob(j).sentiment.subjectivity
#         sentiment.append(sent)
#         pol = TextBlob(j).sentiment.polarity
#         polarity.append(pol)
# print(sentiment, mean(sentiment))
# print('--------')
# print(polarity, mean(polarity))
# print('--------')



def return_tblob(email_text):
    sentiment = []
    polarity = []
    for i in email_text:
        i = i.split('.')
        for j in i:
            sent = TextBlob(j).sentiment.subjectivity
            sentiment.append(sent)
            pol = TextBlob(j).sentiment.polarity
            polarity.append(pol)
    return (sentiment), (polarity)

print(return_tblob(emails))
