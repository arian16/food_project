from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap # pip install flask_bootstrap has to be within venv
import pickle
#import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import gensim

# The below function removes the stop words and tokenize the sentence
def preprocess(text):
    tokens = gensim.utils.simple_preprocess(text)
    stop_words = stopwords.words('english')
    return [tok for tok in tokens if tok not in stop_words]

def word_finder(x):
    y = [elem for elem in negative_words_list if(elem in x)]
    return y

def freq_finder(x):
    y = len(x)
    return y

# List of negative words
negative_words = pd.read_csv('/Users/kristenboyle/Documents/food_project/negative_words.csv', header = None)
negative_words_list = negative_words.iloc[:, 0].tolist()


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/safeTdigest',methods = ['POST', 'GET'])
def safeTdigest():

    if request.method == 'POST':
        result = request.form
        # Loading model from the training set
        with open('model_logistic.pickle', 'rb') as handle:
            model_log = pickle.load(handle)
        # Change the user input data to a dataframe
        df = pd.DataFrame(result, index=[0])

        # Clean and tokenize
        desired_series = df.frequency.tolist()
        series_token = [preprocess(sentence) for sentence in desired_series]
        df['frequency'] = series_token

        # check if the text_clean column has any of the negative words


        df['frequency'] = df['frequency'].apply(word_finder)

        # Find the number of negative words based on the length of each row from 'negative_word'


        df['frequency'] = df['frequency'].apply(freq_finder)

        X_test = df
        grade_outcome = model_log.predict(X_test) # Good: 0, Bad: 1
        if grade_outcome == 0:
            grade = "Good"
            #outcome_prob = 1 - grade_outcome_prob
        else:
            grade = "Bad"
            #outcome_prob = grade_outcome_prob
        #grade = 1 + 2 * int(df.loc[0,"star"]) + 10 * int(df.loc[0,"count"])

        return render_template("index.html", grade_OP = grade)

if __name__ == '__main__':
   app.run(debug = True)
