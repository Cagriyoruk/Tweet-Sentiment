# Import the Google Cloud libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

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