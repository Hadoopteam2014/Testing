from django.http import HttpResponse
import urllib2
import urllib
import time
import requests
from urlparse import urlparse
import oauth2 as oauth
import urlparse
from linkedin import linkedin
from lkdin.models import *
import json
import webbrowser
consumer_key = "75nanr9qwylt2d"
consumer_secret = "UpORpgoDH1iUl2kL"
def index1(request):
 authorize=True
 consumer = oauth.Consumer(consumer_key, consumer_secret)
 request.session['consumer']=consumer
 client = oauth.Client(consumer)
 request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
 resp, content = client.request(request_token_url, "POST")
 request_token = dict(urlparse.parse_qsl(content))
 oauth_token=request_token['oauth_token']
 request.session['oauth_token']=oauth_token
 oauth_token_secret =request_token['oauth_token_secret']
 request.session['oauth_token_secret']=oauth_token_secret
 fopen=open('jsp.js','rb')
 a=fopen.readline()
 b=a.replace('myvar',oauth_token)
 return HttpResponse(b)
def index(request): 
   a=request.session['consumer']
   b=request.session['oauth_token']
   c=request.session['oauth_token_secret']
   q=request.GET.get('oauth_verifier', 'refused')
   oauth_verifier =q
   if oauth_verifier:
    access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
    token = oauth.Token(b,c)
    token.set_verifier(oauth_verifier)
    client = oauth.Client(a, token)
    resp, content = client.request(access_token_url, "POST") 
    access_token = dict(urlparse.parse_qsl(content))
    USER_TOKEN=access_token['oauth_token']
    USER_SECRET=access_token['oauth_token_secret']
    RETURN_URL = 'http://127.0.0.1:8000/lkdn/'
    auth = linkedin.LinkedInDeveloperAuthentication(consumer_key,
    consumer_secret,USER_TOKEN,USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
    app = linkedin.LinkedInApplication(auth)
    x = app.get_profile(selectors=['id', 'firstName', 'lastName', 'location', 'numConnections', 'skills', 'educations','group_memberships','interests','positions'])
    ky=x.keys()
    count=0
    for i in range(len(ky)):
      if ky[i]=="skills":
         count=1
         break
    if count!=1:
      updat_dict={'skills':"null"}
      x.update(updat_dict)
    for i in range(len(ky)):
     if ky[i]=="educations":
         count=1
         break
    if count!=1:
     updat_dict={'educations':"null"}
     x.update(updat_dict)
    for i in range(len(ky)):
     if ky[i]=="location":
         count=1
         break
    if count!=1:
     updat_dict={'location':"null"}
     x.update(updat_dict)
    for i in range(len(ky)):
     if ky[i]=="distance":
         count=1
         break
    if count!=1:
     updat_dict={'distance':"null"}
     x.update(updat_dict)
    grplen= x['groupMemberships']['_count']
    for i in range(grplen):
     grpid = x['groupMemberships']['values'][i]['group']['id']
     grpname = x['groupMemberships']['values'][i]['group']['name']
     p1=usergroup(Userids=x['id'],groupid = grpid, groupname=grpname)
     p1.save(using="linkedin")
     p5 = groups(groupid=grpid,groupname=grpname)
     p5.save(using="linkedin")
    edulen=x['educations']['_total']
    for i in range(edulen):
     deg = x['educations']['values'][i]['degree']
     schl = x['educations']['values'][i]['schoolName']
     eduid = x['educations']['values'][i]['id']
     startDate = x['educations']['values'][i]['startDate']
     endDate = x['educations']['values'][i]['endDate']
   #fieldofstudy = x['educations']['values'][i]['fieldOfStudy']
     p2=usereducation(Userids = x['id'],eduid=eduid,school=schl,degree=deg,startDate=startDate,endDate=endDate)
     p2.save(using="linkedin")
    skillen = x['skills']['_total']
    for i in range(skillen):
     skill=x['skills']['values'][i]['skill']['name']
     skillid=x['skills']['values'][i]['id']
     p3=Userskill(Userids = x['id'],skillid=skillid,skillname=skill)
     p3.save(using="linkedin")
    poslen = x['positions']['_total']
    for i in range(poslen):
     compid = x['positions']['values'][i]['company']['id']
     compname = x['positions']['values'][i]['company']['name']
     p6=userposition(ids=x['id'],companyid=compid,compname=compname)
     p6.save(using="linkedin") 
    x1= app.get_company_updates(compid)
    for j in range(x1['_count']):
     updateKey = x1['values'][j]['updateKey']
     timestamp = x1['values'][j]['timestamp']
     numLikes = x1['values'][j]['numLikes']
     updatecontent=x1['values'][j]['updateContent']['companyJobUpdate']['job']['description']
     updatecomments=x1['values'][j]['updateComments']
     p7 = company(updateKey=updateKey,companyid=compid,timestamp=timestamp,numLikes=numLikes,updatecomments=updatecomments)
     p7.save(using="linkedin")
    p5 = userprofile(firstname = x['firstName'], lastname = x['lastName'], Userids = x['id'], location = x['location'],numconnections = x['numConnections'],interests=x['interests'])
    p5.save(using="linkedin")
    return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>")
   else:
     return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>")

