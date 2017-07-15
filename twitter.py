/*A twitter trend script by Mukul Sharma
You need to enter the keyword (any celebrity, any noun, anything)
The script will search the most recent 1000 tweets which contains that particular keyword
As of now it can only search in english language
but I will add functionlity for other languages*/
import tweepy
from textblob import TextBlob
from statistics import *
consumer_key= 'VqMbFt9Vzzm1tM4u9jcuERpi2'
consumer_secret = '3Nxv1KiMiVKtcIcyO5X3JTbyiFEO8TpWQcA3JeOGP2efZJMgBG'
access_token='3277407996-wlDeJZ9lJ3XJ7FtHCSd9cUKuHkABe7XNCMk1Jpm'
access_token_secret='27cTxLLeV1X13qHXMSij0cnSdHDjdPzpz3dIArzxmBciD'
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