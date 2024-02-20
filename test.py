import tweepy

# Twitter APIキーの設定
consumer_key = 'QLqXwOGtAhdICKZQWgy0aVc17'
consumer_secret = '4GmSCmanDP77CPrY0nPPI0RD9QKsrLN1AEPP72ZrF0RYc8sQ6D'
access_token = '860371080405336064-pAgEhJNBQraTT3GGlIVUkTbcllEEdgV'
access_token_secret = 'uEq7X6c7hzBMZXHO0RdODSDHNB4vQpJtlYTn61TPaNojl'

# Use OAuthHandler to set the credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize the API object
api = tweepy.API(auth)

# Check if authentication was successful
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
try:
    api.update_status("Hello World")
    print("Tweet posted successfully")
except tweepy.errors.TweepyException as e:
    print(f"Error posting tweet: {e}")
