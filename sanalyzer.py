import tweepy
from textblob import TextBlob 


consumerkey = 'PRIVATE KEY
consumerkey_s = 'SECRET KEY'

token = 'PRIVATE TOKEN'
token_s = 'SECRET TOKEN'

auth = tweepy.OAuthHandler (consumerkey, consumerkey_s)
auth.set_access_token (token, token_s)

api = tweepy.API (auth)

tweets = api.search ('Pakistan')

for tweet in tweets:
	print (tweet.text)

	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
	print ("")
