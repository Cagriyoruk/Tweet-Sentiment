# Import the twitter API
import tweepy
# Define a function returns the twitter feed
def get_tweet():
  twitter_feed = []
  # Authorize 
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key,access_secret)
  auth_tweet = tweepy.API(auth)
  public_tweets = auth_tweet.home_timeline(count = 40)
  for tweet in public_tweets:
    twitter_feed = twitter_feed + [tweet.text]
  return twitter_feed