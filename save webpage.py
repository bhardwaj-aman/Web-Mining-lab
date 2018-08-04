import urllib3

http = urllib3.PoolManager()
r = http.request('get', 'https://en.wikipedia.org/wiki/Template_talk:Did_you_know')

with open('C:\Aman\padhaii\sem 5\web mining\page list\page60.html', 'wb') as fid:
    fid.write(r.data)
