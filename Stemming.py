# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:52:05 2018

@author: justf
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
lund = " What the hell are you riding on you piece of shit, dont you ever ride on that again, or i will ride your mom as i was riding your sister"
wrd = word_tokenize(lund)
for w in  wrd:
    print(ps.stem(w))