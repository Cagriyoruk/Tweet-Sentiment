# Import the twitter API
import tweepy

# Import the Google Cloud libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

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

# Define a function to analyze the sentiment
def language_analysis(text):
  client = language.LanguageServiceClient()
  document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document=document).document_sentiment
  return sentiment

# Define a function to return the number of the state of the tweets
def sentiment_number():
  x,y,z = 0,0,0
  if sentiment.score > 0:
    x = x + 1
  elif sentiment.score < 0:
    y = y + 1
  else:
    z = z + 1
  return x,y,z

# Main Function Getting Tweets and Sentiment
sentiment_number_list = [0,0,0]
for tweet in get_tweet():
  print(tweet)
  sentiment = language_analysis(tweet)
  print(' The Sentiment Score is:',sentiment.score,'\n','The Sentiment Magnitude is:',sentiment.magnitude)
#Sentiment Number Function Part
  for i in range(3):
    sentiment_number_list[i] = sentiment_number_list[i] + list(sentiment_number())[i]
print('The total number of Positive tweets:',sentiment_number_list[0])
print('The total number of Negative tweets:',sentiment_number_list[1])
print('The total number of Vague tweets:',sentiment_number_list[2])