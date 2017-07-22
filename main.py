"""A twitter trend script by Mukul Sharma
You need to enter the keyword (any celebrity, any noun, anything)
The script will search the most recent 1000 tweets which contains that particular keyword
As of now it can only search in english language
but I will add functionlity for other languages"""
import tweepy
from textblob import TextBlob
from statistics import *
consumer_key= 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
subject = input('Enter the keyword that you want to search ')
list = []
neutral=0
positive=0
negative=0
count =0
for tweet in tweepy.Cursor(api.search, q=subject).items(1000):
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    list.append(analysis.sentiment.polarity)
    count+=1
print ("Average Polarity" + str(mean(list)) )   
for i in list:
    if i==0.0:
       neutral+=1
    if i>0.0:
       positive+=1
    if i<0.0:
       negative+=1
print ("Total Neutral :" + str(neutral))
print ("Total Positive :" + str(positive))
print("Total Negative :" + str(negative))
print("Total Tweets Searched" + str(count))