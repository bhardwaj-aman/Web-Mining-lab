# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:07:41 2018

@author: justf
"""
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from sklearn.feature_extraction.text import TfidfVectorizer

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

file = "C:\Aman\padhaii\sem 5\web mining\page list\page10.html"
f=open(file, 'r+', encoding="utf8")
tex = f.read()
text = [text_from_html(tex),
		"The dog.",
		"The fox"]
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

