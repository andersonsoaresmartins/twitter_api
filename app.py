# Import library and keys 
import tweepy
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, BEARER_TOKEN

# Enter the text of your post 
tweet = "Tweet posted using tweepy!"


client = tweepy.Client(
                        bearer_token=BEARER_TOKEN,
                        consumer_key=API_KEY,
                        consumer_secret=API_KEY_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET)

# Creating tweet and posting
response = client.create_tweet(text = tweet)

print(response)

