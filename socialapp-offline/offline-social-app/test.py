from django.http import HttpResponse
import json
from urllib2 import URLError
import urllib2
import urllib
import apiclient.discovery
from apiclient.discovery import build
from gplus.models import UserProfile
url="https://www.googleapis.com/plus/v1/people/me?"
data={}
data['access_token']="ya29.JQBD2FLu3fSlHx8AAACi7bw4bsdy_QJ9sd6rR9gAUJDC0iFmIKpMSLdKwg"
url_values=urllib.urlencode(data
full_url=url+url_values
data2=urllib2.urlopen(full_url)
a=data2.read()
b=json.loads(a)
c=b.keys()
count=0
for i in range(len(c)):
    if c[i]=="emails":
       count=1
       break
if count!=1:
   updat_dict={'emails':[{'value':"nill"}]}
   b.update(updat_dict)
for i in range(len(c)):
    if c[i]=="ageRange":
       count=1
       break
if count!=1:
   updat_dict={'ageRange':{'min':0}}
   b.update(updat_dict)
for i in range(len(c)):
    if c[i]=="language":
       count=1
       break
if count!=1:
   updat_dict={'language':'nill'}
   b.update(updat_dict)
for i in range(len(c)):
    if c[i]=="name":
       count=1
       break
if count!=1:
   updat_dict={'name':{'familyName':'nill','givenName':'nill'}}
   b.update(updat_dict)
count1=0
for i in range(len(c)):
    if c[i]=="gender":
        count1=1
        break
if count1!=1:
   updat_dict={'gender':'nill'}
   b.update(updat_dict)
print b

print b['emails'][0]['value']
print b['gender']
print b['id']
print b['displayName']
print b['name']['familyName']
print b['name']['givenName']
print b['ageRange']['min']
print b['language']
print b['circledByCount']

#p1=UserProfile(userid=b['id'],gender=b['gender'],email=b['emails'][0]['value'],name=b['displayName'],familyname=b['name']['familyName'],givenname=b['name']['givenName'],agerange=b['ageRange']['min'],language=b['language'],circledByCount=b['circledByCount'])
#p1.save()

