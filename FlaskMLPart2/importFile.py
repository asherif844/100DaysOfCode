import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv('FlaskMLPart2/data/YoutubeSpamMergedData.csv')
df_data = df[['CONTENT', 'CLASS']]
df_x = df_data['CONTENT']
df_y = df_data.CLASS
df_x = df_x.values
df_y = df_y.values
corpus = df_x 
cv = CountVectorizer()
x = cv.fit_transform(corpus)

x_train, x_test, y_train, y_test = train_test_split(x, df_y, test_size = 0.25, random_state = 12345)
clf = MultinomialNB()
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
# y_predict = clf.predict(x_test)
# print(accuracy_score(y_test, y_predict))
# print(clf.score(x_test, y_test))

print(type(df_data.values))
print(type(df_data.toarray()))