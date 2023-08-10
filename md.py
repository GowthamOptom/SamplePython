

'''
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = client["employ"]

mycol = mydb.collections

rec = [{
    "name": "gow",
    "empno": 1
}]

mycol.insert_one(rec)
'''



'''
Music recommendation using Decision tree classifier - 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

m_data = pd.read_csv('music.csv')
x = m_data.drop(columns = ['genre'])
y = m_data['genre']

model = DecisionTreeClassifier()
model.fit(x, y)
predictions = model.predict([ [22, 1], [24, 0] ])
predictions

Movie recommendation - 
import pandas as pd
movies = pd.read_csv("movies.csv")
movies
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ngram_range = (1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices][::-1]
    return results
similarity
import ipywidgets as widgets
from IPython.display import display
movie_input = widgets.Text(value = "Toy Story", description = "Movie Title", disabled = False)
movie_list = widgets.Output()

def on_type(data):
    with movie_list:
        movie_list.clear_output()
        title = data["new"]
        if len(title) > 4:
            display(search(title))
            
movie_input.observe(on_type, names = "value")

display(movie_input, movie_list)
Practice these two projects and post your doubts.
'''



#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    else:
        if n>=2 & n<=5:
            print("Not Weird")
        elif n>=6 & n<=20:
            print ("Weird")
        else:
            "Not Weird" 