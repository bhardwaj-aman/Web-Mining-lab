from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import math
from collections import Counter
i=11
while i<51:
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
    file1= "C:\Aman\padhaii\sem 5\web mining\page list\page%d.html" % i
    f=open(file, 'r+', encoding="utf8")
    f1=open(file1, 'r+', encoding="utf8")
    text = f.read()
    text1 = f1.read()
    #print(text_from_html(text))
    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
    
    
    def text_to_vector(text):
        word = re.compile(r'\w+')
        words = word.findall(text)
        return Counter(words)
    
    
    def get_result(content_a, content_b):
        text1 = content_a
        text2 = content_b
    
        vector1 = text_to_vector(text1)
        vector2 = text_to_vector(text2)
    
        cosine_result = get_cosine(vector1, vector2)
        return cosine_result
    mystring = text_from_html(text).strip()
    mystring1 = text_from_html(text1).strip()  # the while loop will leave a trailing space, 
                      # so the trailing whitespace must be dealt with
                      # before or after the while loop
 
    while '  ' in mystring:
        mystring = mystring.replace('  ', ' ')
    while '  ' in mystring1:
        mystring1 = mystring1.replace('  ', ' ')
    while '...' in mystring:
        mystring = mystring.replace('...', '.')
    while '^ ' in mystring:
        mystring = mystring.replace('^ ', '')
    while '...' in mystring1:
        mystring = mystring1.replace('...', '.')
    while '^ ' in mystring1:
        mystring = mystring1.replace('^ ', '')
        
    print (get_result('mystring', 'mystring1'))
    i+=1
