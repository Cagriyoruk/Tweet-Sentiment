# Tweet-Sentiment
Tweet-Sentiment. Returns the tweets and the sentiment analysis. Even gives the number of positive,negative and vague tweets. Awesome right ?
# Our System Architecture
![Tweetsentimentarch](https://user-images.githubusercontent.com/55101879/65399206-4cc8d900-dd89-11e9-985a-49c0dd987bcb.png)

# API
You need to get credentials(API Key's) from both twitter developer and google cloud platform to use this program.

There is a line for entering your keys as consumer_key,consumer_secret,access_key and access_secret.

For Twitter api you can visit this website: https://www.tweepy.org/

For Google NLP api you can visit this website: https://cloud.google.com/natural-language/

For the Google Credentials visit this website: https://cloud.google.com/natural-language/docs/quickstart-client-libraries#client-libraries-usage-python

There are several steps to get a google Credential:

1- Create a google cloud account.

2- Create and Set up a project.

3- Download the JSON file that contains your service account key.

4- Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file you downloaded. (This variable only applies to your current shell session, so if you open a new session, set the variable again.)

5-Install the client library.

After Installing and putting the Keys and activating the API. The program should work.

# Here is an Example of output:

![Tweet_Sentiment_example](https://user-images.githubusercontent.com/55101879/64929085-45d12200-d7ef-11e9-9a16-7317348924b1.png)
