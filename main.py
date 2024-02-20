import tweepy
from gtts import gTTS
import time

# Twitter APIキーの設定
consumer_key = 'QLqXwOGtAhdICKZQWgy0aVc17'
consumer_secret = '4GmSCmanDP77CPrY0nPPI0RD9QKsrLN1AEPP72ZrF0RYc8sQ6D'
access_token = '860371080405336064-pAgEhJNBQraTT3GGlIVUkTbcllEEdgV'
access_token_secret = 'uEq7X6c7hzBMZXHO0RdODSDHNB4vQpJtlYTn61TPaNojl'

# Tweepyを初期化
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイートを取得して読み上げる
def read_tweets(username, count=10):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")

    for tweet in tweets:
        user_name = tweet.user.screen_name
        text = tweet.full_text

        print(f"{user_name}: {text}")

        # テキスト読み上げエンジンを使用してツイートを読み上げる
        tts = gTTS(text, lang='ja')
        tts.save('tweet.mp3')
        # 作成した音声ファイルを再生
        # ここでは例として、OS標準のプレーヤーを使用しています
        # 必要に応じて、他の方法やライブラリを使用することができます
        # 例: https://pypi.org/project/playsound/
        import os
        os.system('start tweet.mp3')
        time.sleep(5)  # 5秒待機

# ユーザーのツイートを読み上げる例
read_tweets('target_user_screen_name')
