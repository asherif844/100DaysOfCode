from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['POST'])
def predict():
    df = pd.read_csv('FlaskMLPart2/data/YoutubeSpamMergedData.csv')
    df_data = df[['CONTENT', 'CLASS']]
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    # df_x = df_x.values
    # df_y = df_y.values
    corpus = df_x
    cv = CountVectorizer()
    x = cv.fit_transform(corpus)

    x_train, x_test, y_train, y_test = train_test_split(x, df_y, test_size=0.25, random_state=12345)
    clf = MultinomialNB()
    clf.fit(x_train, y_train)
    clf.score(x_test, y_test)

    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        vect = cv.transform(data).toarray()
        myPrediction = clf.predict(vect)
    return render_template('result.html', prediction = myPrediction)



if __name__ == '__main__':
    app.run(debug=True)

