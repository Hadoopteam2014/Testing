from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import urllib
import requests
import oauth2 
import urlparse
import json
from twitter.oauth import OAuth
import twitter
from twitterapp.models import *
from twitter.oauth_dance import parse_oauth_tokens
from twitter.oauth import read_token_file, write_token_file
from twitter.oauth_dance import oauth_dance
import webbrowser
from twitterapp.html import test
consumer_key = 'RJZMooGv5i6u4BiJ5bh1wdj87'
consumer_secret = 'xuv7MgW5MaRnVLCFTQxy1UNjjJVayKcgCSROSzQcJHwZlxZ2sK'
app_name = "Tweetwissen"
def index(request):
  twitter1 = twitter.Twitter(auth=twitter.OAuth('', '', consumer_key, consumer_secret),format='', api_version=None)
  oauth_token, oauth_token_secret = parse_oauth_tokens(twitter1.oauth.request_token()) 
  oauth_url = ('https://api.twitter.com/oauth/authorize?oauth_token=' + oauth_token)
  request.session['oauth_token']=oauth_token
  request.session['oauth_token_secret']=oauth_token_secret
  fopen=open('jsp1.js','rb')
  a=fopen.readline()
  b=a.replace('myvar',oauth_token)
  return HttpResponse(b)
def index1(request):
  a1=request.session['oauth_token']
  b1=request.session['oauth_token_secret']
  q=request.GET.get('oauth_verifier', '')
  oauth_verifier =q
  if oauth_verifier:
   access_token_url = "https://api.twitter.com/oauth/access_token"
   token = oauth2.Token(a1,b1)
   token.set_verifier(oauth_verifier)
   consumer = oauth2.Consumer(consumer_key,consumer_secret)
   client = oauth2.Client(consumer, token)
   resp, content = client.request(access_token_url, "POST")
   access_token = dict(urlparse.parse_qsl(content))
   twitter_access_token = access_token['oauth_token']
   twitter_access_token_secret = access_token['oauth_token_secret']
   userid = access_token['user_id']
   screenname = access_token['screen_name']
   load_url = "https://api.twitter.com/1.1/account/verify_credentials.json"   
   token1 = oauth2.Token(key=twitter_access_token, secret=twitter_access_token_secret)
   client1 = oauth2.Client(consumer, token1)
   resp1, content1 = client1.request(load_url)
   a=json.loads(content1)
   for i in range(len(a)):
       user_profile = Userprofile(userid=a['id'],username=a['name'],location=a['location'],language=a['lang'],Description=a['description'],screen_name=a['screen_name'])
       user_profile.save(using="twitter")
   frnds_url = "https://api.twitter.com/1.1/friends/list.json"  
   client2 = oauth2.Client(consumer, token1)
   resp2, content2 = client2.request(frnds_url)
   b=json.loads(content2)
   for j in range(len(b['users'])):
       frnds = Frnds(frndid=b['users'][j]['id'],frndname=b['users'][j]['name'],userid=a['id'],location=b['users'][j]['location'])
       frnds.save(using="twitter")
   followrsurl = "https://api.twitter.com/1.1/followers/list.json"
   client3 = oauth2.Client(consumer, token1)
   resp3, content3 = client3.request(followrsurl)
   c=json.loads(content3)
   for q in range(len(c['users'])):
     try:
       followers = Followers(userid=a['id'],followerdid=c['users'][q]['id'],followername=c['users'][q]['name'],location=c['users'][q]['location'])
       followers.save(using="twitter")
     except:
       print ""
   favorurl = "https://api.twitter.com/1.1/favorites/list.json"
   client4 = oauth2.Client(consumer, token1)
   resp4 , content4 = client4.request(favorurl)
   d=json.loads(content4)
   for r in range(len(d)):
       favour = Favourites(favourid=d[r]['id'],favourname=d[r]['text'])
       favour.save(using="twitter")  
   return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>")
  else:
   return HttpResponse("<script type='text/javascript'>d=window.open('http://www.google.com','_self');d.close();</script>") 
      
   
   

        


