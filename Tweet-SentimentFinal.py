# Copyright 2019 Cagri Yoruk cyoruk@bu.edu
# Copyright 2019 Suli Hu sulihu@bu.edu

# Import the Google Cloud libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Import the twitter library
import tweepy
# Define a function to get
def get_tweet():
  twitter_feed = []
  # Authorize 
  auth = tweepy.OAuthHandler("XXXXXXXXXX", "XXXXXXXXXX")
  auth.set_access_token("XXXXXXXXXX","XXXXXXXXXX")
  auth_tweet = tweepy.API(auth)
  while 1:
    print("What do you want to do?","\n","1-Get tweets from my feed","\n","2-Get tweets from a user")
    select = int(input())
    if select == 1:
      numberoftweets = int(input("How many tweets do you want?"))
      tweets = auth_tweet.home_timeline(count = numberoftweets)
      break
    elif select == 2:
      numberoftweets = int(input("How many tweets do you want?"))
      name = input("Enter the user name:")
      tweets = auth_tweet.user_timeline(id = name,count = numberoftweets)
      break
    else:
      print("What the hell are you doing???","\n","Try AGAIN!!!")
  for tweet in tweets:
    twitter_feed = twitter_feed + [tweet.text]
  return twitter_feed

# Define a function to analyze the sentiment
def language_analysis(text):
  client = language.LanguageServiceClient()
  document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document=document).document_sentiment
  return sentiment

# Define a function to save tweets in 3 lists by positive,negative or neutral
# Sentiment score and magnitute is also saved accordingly.
# Total number is counted for each type.
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
# Define a function to print tweets in pos/neg/neu
def print_list(lst):
  print("---BEGIN-------------")
  for e in lst:
    print(e)
  print("---END-------------")
  return
# Main Function
for tweet in get_tweet():
  sentiment_list(tweet)
# Get users inputs to define types and quit the program 
while 1:
  list_sel = input("\n"+"What do you want to see (positive/negative/neutral)"+"\n"+"type Q to quit"+"\n")
  if list_sel == "positive":
    print_list(pos)
    print("The total number of Positive Tweets: ",totalP)
  if list_sel == "negative":
    print_list(neg)
    print("The total number of Negative Tweets: ",totalN)
  if list_sel == "neutral":
    print_list(nea)
    print("The total number of Neutral Tweets: ",totalE)
  if list_sel == "Q":
    break
  else:
    print("Please try again")
