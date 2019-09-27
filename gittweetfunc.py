# Copyright 2019 Cagri Yoruk cyoruk@bu.edu

# Import the twitter library
import tweepy
# Define a function to get the tweets.
def get_tweet():
  twitter_feed = []
  # Authorize 
  auth = tweepy.OAuthHandler("2vmFnAMVIO8NfLE6QlFrf4Rc3", "q8xCQGZx0YHC8cQngdnmpaQ5DeKJAx1fS0GHkH9b06tUp3T6Yi")
  auth.set_access_token("1171098217959677952-U7TzAWtJ98ZP7iLDNctKoWNBVvmn6C","muelgRZWemk3tojNB3Bz2zr0ckc6hEQC51N5rhOR1Y9Km")
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