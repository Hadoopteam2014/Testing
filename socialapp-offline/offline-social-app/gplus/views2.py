from django.http import HttpResponse
import json
from urllib2 import URLError
import urllib2
import urllib
import apiclient.discovery
from apiclient.discovery import build
from gplus.models import UserProfile
def index(request,token):
    url="https://www.googleapis.com/plus/v1/people/me?"
    data={}
    #data['userId']="me"
    data['access_token']=token
    url_values=urllib.urlencode(data)
    full_url=url+url_values
    data2=urllib2.urlopen(full_url)
    a=data2.read()
    b=json.loads(a)
    c=b.keys()
    count=0
    try:
     for i in range(len(c)):
      if c[i]=="emails":
       count=1
       break
     if count!=1:
      updat_dict={'emails':[{'value':"nill"}]}
      b.update(updat_dict)
     count1=0
     for i in range(len(c)):
      if c[i]=="ageRange":
       count1=1
       break
     if count1!=1:
      updat_dict={'ageRange':{'min':0}}
      b.update(updat_dict)
     count2=0
     for i in range(len(c)):
      if c[i]=="language":
       count2=1
       break
     if count2!=1:
      updat_dict={'language':'nill'}
      b.update(updat_dict)
     count3=0
     for i in range(len(c)):
      if c[i]=="name":
       count3=1
       break
     if count3!=1:
      updat_dict={'name':{'familyName':'nill','givenName':'nill'}}
      b.update(updat_dict)
     count4=0
     for i in range(len(c)):
      if c[i]=='gender':
       count4=1
       break
     if count4!=1:
      updat_dict={'gender':'nill'}
      b.update(updat_dict)
    except:
     print "sorry"
    p1=UserProfile(userid=b['id'],gender=b['gender'],email=b['emails'][0]['value'],name=b['displayName'],familyname=b['name']['familyName'],givenname=b['name']['givenName'],agerange=b['ageRange']['min'],language=b['language'],circledByCount=b['circledByCount'])
    p1.save()
    return HttpResponse("thanks for response")
