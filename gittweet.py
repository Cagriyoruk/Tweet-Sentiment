# Copyright 2019 Cagri Yoruk cyoruk@bu.edu

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