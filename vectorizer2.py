from sklearn.feature_extraction.text import CountVectorizer
import nltk, string, numpy
nltk.download('wordnet') # first-time use only
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
LemVectorizer.fit_transform("C:\Aman\padhaii\sem 5\web mining\page list\sample.txt")
print (LemVectorizer.vocabulary_)