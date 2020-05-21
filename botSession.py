import json
import tweepy
import logging
from queue import Queue
from telegram import Bot
from botInfo import tg_id
from botMarkov import gen_model
from botTools import query_token
from telegram.ext import Dispatcher
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler(misfire_grace_time=60)

twitter_token = json.loads(query_token('luxun'))
token_auth = tweepy.OAuthHandler(twitter_token['consumer_key'], twitter_token['consumer_secret'])
token_auth.set_access_token(twitter_token['access_token'], twitter_token['access_token_secret'])
lx_twi = tweepy.API(token_auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

lx_model = gen_model()

lx_tg = Bot(query_token(tg_id))
update_queue = Queue()
dp = Dispatcher(lx_tg, update_queue, use_context=True)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)
