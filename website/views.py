from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import os
import requests

import tweepy
from textblob import TextBlob

### For Logging purposes to console.. disable in production
# import logging
# logger = logging.getLogger(__name__)

def twitterHero(data,size):
    consumer_key=os.environ.get('CONSUMER_KEY')
    consumer_secret=os.environ.get('CONSUMER_SECRET')

    access_token=os.environ.get('ACCESS_TOKEN')
    access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')

    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api=tweepy.API(auth)

    S=[]
    counter=[0,0,0] # positive, negative, neutral
    for tweet in tweepy.Cursor(api.search, q=data, rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(size):
        # logger.log(100,tweet)  # MASSIVE DATA DUMP for debugging
        analysis=TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            res='positive'
            counter[0]+=1
        elif analysis.sentiment.polarity == 0:
            res='neutral'
            counter[2]+=1
        else:
            res='negative'
            counter[1]+=1
        S.append((tweet.text,analysis.sentiment,res,tweet.user.name,tweet.user.profile_image_url_https,tweet.user.screen_name))
    positivePer=(counter[0]/size)*100
    negativePer=(counter[1]/size)*100
    neutralPer=(counter[2]/size)*100
    S.append((positivePer,negativePer,neutralPer))
    return S


def index(request):
    return render(request,'website/home.html',{})


def form_data(request):
    try:
        data=request.POST['q']
        size=int(request.POST['size'])
    except MultiValueDictKeyError:
        data='data science'
        size=50
    if data=='':
        data='data science'
    S=twitterHero(data,size)
    # logger.log(100,"Called function.")
    posPer,negPer,ntrPer=S[-1][0],S[-1][1],S[-1][2]
    del S[-1]
    return render(request,'website/index.html',{'data':S,'search':data,'posPer':posPer,'negPer':negPer,'ntrPer':ntrPer})
