import json
import tweepy
from botMarkov import gen_model
from botTools import query_token
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler(misfire_grace_time=60)

twitter_token = json.loads(query_token('luxun'))
token_auth = tweepy.OAuthHandler(twitter_token['consumer_key'], twitter_token['consumer_secret'])
token_auth.set_access_token(twitter_token['access_token'], twitter_token['access_token_secret'])
lx = tweepy.API(token_auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

lx_model = gen_model()
