# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:49:20 2018

@author: justf
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
lauda= " You are a filthy piece of shit"
stop_words= set(stopwords.words("english"))
wrds= word_tokenize(lauda)
filtered = []
for w in wrds:
    if w not in stop_words:
        filtered.append(w)
print(filtered)        
