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

# Define a function to make 3 lists
pos,neg,nea =[],[],[]

totalP =0
totalN =0
totalE =0
def sentiment_list(twts):
  global totalP
  global totalN 
  global totalE
  sentiment = language_analysis(twts)
  if sentiment.score > 0:
    pos.append(twts)
    pos.append("Sentiment Score:") 
    pos.append(sentiment.score)
    pos.append("Magnitude:")
    pos.append(sentiment.magnitude)
    pos.append("---")
    totalP = totalP +1
  elif sentiment.score < 0:
    neg.append(twts)
    neg.append("Sentiment Score:")
    neg.append(sentiment.score)
    neg.append("Magnitude:")
    neg.append(sentiment.magnitude)
    neg.append("---")
    totalN = totalN +1
  else:
    nea.append(twts)
    nea.append("Sentiment Score:")
    nea.append(sentiment.score)
    nea.append("Magnitude:")
    nea.append(sentiment.magnitude)
    nea.append("---")
    totalE = totalE +1
  return
#Define a function to print tweets in pos/neg/neu
def print_list(lst):
  print("---BEGIN-------------")
  for e in lst:
    print(e)
  print("---END-------------")
  return
#main function
for tweet in get_tweet():
  #print(tweet)
  sentiment_list(tweet)
while 1:
  list_sel = input("\n"+"What do you want to see (positive/negative/neatural)"+"\n"+"type Q to quit"+"\n")
  if list_sel == "positive":
    print_list(pos)
    print("The total number of Positive Tweers: ",totalP)
  if list_sel == "negative":
    print_list(neg)
    print("The total number of Negiative Tweers: ",totalN)
  if list_sel == "neatural":
    print_list(nea)
    print("The total number of Netural Tweers: ",totalE)
  if list_sel == "Q":
    break
  else:
    print("please try again")
