from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


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

file = "C:\Aman\padhaii\sem 5\web mining\page list\page39.html"
f=open(file, 'r+', encoding="utf8")
text = f.read()
mystring = text_from_html(text).strip()  # the while loop will leave a trailing space, 
                  # so the trailing whitespace must be dealt with
                  # before or after the while loop
while '  ' in mystring:
    mystring = mystring.replace('  ', ' ')
while '...' in mystring:
    mystring = mystring.replace('...', '.')
while '^ ' in mystring:
    mystring = mystring.replace('^ ', '')    
    
print(mystring)
