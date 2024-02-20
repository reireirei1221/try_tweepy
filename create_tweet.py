import tweepy

# Twitter APIキーの設定
consumer_key = 'QLqXwOGtAhdICKZQWgy0aVc17'
consumer_secret = '4GmSCmanDP77CPrY0nPPI0RD9QKsrLN1AEPP72ZrF0RYc8sQ6D'
access_token = '860371080405336064-pAgEhJNBQraTT3GGlIVUkTbcllEEdgV'
access_token_secret = 'uEq7X6c7hzBMZXHO0RdODSDHNB4vQpJtlYTn61TPaNojl'

client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)
client.create_tweet(text="Hello World")