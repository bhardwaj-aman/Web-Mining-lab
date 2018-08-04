# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:32:42 2018

@author: justf
"""

import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.corpus import inaugural
train = inaugural.raw("2009-Obama.txt")
sample= inaugural.raw("1865-Lincoln.txt")
custom_tokenizer= PunktSentenceTokenizer(train)
tokenized = custom_tokenizer.tokenize(sample)
def process():
    for i in tokenized:
        words= nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)
process()
