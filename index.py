import discord
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


# Discord credentials
TOKEN = os.getenv('TOKEN')

# Twitter credentials
bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


# Authenticate with Twitter
twitterClient  = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token=access_token, access_token_secret=access_token_secret)

# Discord Config
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
discordClient = discord.Client(intents=intents)
message_history = []

@discordClient.event
async def on_ready():
    print(f'{discordClient.user.name} has connected to Discord!')

@discordClient.event
async def on_message(message):
    global message_history
    # Store the message content
    message_history.append(message.content)

    # Create a tweet
    if twitterClient is not None:
        tweet = message.content
        try:
            twitterClient.create_tweet(text=tweet)
        except Exception as e:
            print(f"Error creating tweet: {e}")
    else:
        print("Twitter authentication failed. Tweets cannot be posted.")

discordClient.run(TOKEN)
