import tweepy
from textblob import TextBlob 


consumerkey = 'u0RTgv7uGOZwfeud9680mxcmw'
consumerkey_s = '1UkUZMmiKK8546iEa0gNKoOj4FgVUhBBiZWJ0EXrS1hw6GqA4t'

token = '280476027-RaFt1yujEmrSPDPKlyNdojjVAgmaHhWepU6MgBLw'
token_s = 'TTvhj4qs6GA0KzGfqKvH2q4yQeiFcNfTzs1lkx60SXxBt'

auth = tweepy.OAuthHandler (consumerkey, consumerkey_s)
auth.set_access_token (token, token_s)

api = tweepy.API (auth)

tweets = api.search ('Pakistan')

for tweet in tweets:
	print (tweet.text)

	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
	print ("")