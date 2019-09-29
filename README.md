# Tweet-Sentiment
Tweet-Sentiment. Returns the tweets and the sentiment analysis and gives the number of positive,negative and neutral tweets. Awesome right ?
# Our System Architecture
![Tweetsentimentarch](https://user-images.githubusercontent.com/55101879/65399206-4cc8d900-dd89-11e9-985a-49c0dd987bcb.png)

# User Stories
#Sprint 1

    • As a user, I want to get a summary of my feed. -1

    • As a user, I want the sentiment analysis of my feed. Score/magnitude for each tweet

    • As a user, I want the number of positive, negative and the vague tweets. -1 -numbers

    • As a user, I want to be able to select the tweet amount so that I can read them based on the time I have.

#Sprint 2

    • As a user, I want to access the positive and negative number of tweets from the other user I care, so that I can know more about him/her.-2

    • As a News Company, I want to access the most important tweets, so that I can find the eye-catching topics easily. 

    • As a Mental Health Care Company, I want to access the negative number of tweets of a person, so that I can provide better consulting. -2 -givennumber - negative

    • As a Data Handling Company, I want to access the Vague tweets so that I can analyze the data.  -2 -givennumber -neutral


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

![In_Action](https://user-images.githubusercontent.com/55101879/65839353-724e6900-e2da-11e9-8034-891b23b670d6.png)
