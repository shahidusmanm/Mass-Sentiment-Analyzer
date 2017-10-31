import tweepy
from textblob import TextBlob 

#Read Twitter credentials from a text file
cred = open ('credentials.txt', 'r')

consumerkey = cred.readline ().replace ('\n', '')
consumerkey_s = cred.readline ().replace ('\n', '')
token = cred.readline ().replace('\n', '')
token_s = cred.readline ().replace('\n', '')

auth = tweepy.OAuthHandler (consumerkey, consumerkey_s)
auth.set_access_token (token, token_s)

api = tweepy.API (auth)

tweets = api.search ('Pakistan')

for tweet in tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
	print ("")