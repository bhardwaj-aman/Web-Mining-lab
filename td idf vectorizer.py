from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
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
#print(vectorizer.vocabulary_)
#print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
 #summarize encoded vector
#print(vector.shape)
tf_matrix = vectorizer.transform(text).toarray()
print (len(tf_matrix))
#print(vector.toarray())


def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

# the counts we computed above
sentence_m = np.array(tf_matrix) 
sentence_h = np.array([[0 for x in range(3)] for y in range(len(sentence_m))] )
sentence_w = np.array([0, 0, 0, 1, 0, 0, 1, 1, 1])
print(len(sentence_m))
# We should expect sentence_m and sentence_h to be more similar
print(cos_sim(sentence_m, sentence_h)) # 0.5
