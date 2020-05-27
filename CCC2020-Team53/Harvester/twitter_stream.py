# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:20:43 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""
import time
import tweepy
import json
from pathlib import Path
Path('recent_tweets.json').touch()

def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(json.loads(data)) + "\n")
    outfile.close()


class StreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=30):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = 'recent_tweets.json'
        super(StreamListener, self).__init__()
        
    def on_data(self, data):
        try:
            if (time.time() - self.start_time) < self.limit:
                write_file(self.saveFile,data)
                return True
            else:
                return False
        except BaseException as e:
            print("Error: %s" % str(e))
        return True
          
    # restriction of max rate limit
    def on_error(self, status_code):
        if status_code == 420:
                self.on_timeout()
    # sleep for 10 minutes
    def on_timeout(self):
        time.sleep(600)

def start_stream(credentials, gridDetails):
        try:
            streamListener = StreamListener()
            auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
            auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
            api = tweepy.API(auth)
            # extended gives the full texty field
            stream = tweepy.Stream(auth = api.auth, listener=streamListener,tweet_mode='extended')
            # This line filter Twitter Streams to capture data by the location: 
            stream.filter(locations=gridDetails, languages=['en'])
        except Exception as e:
            print("Error: Restart the stream ", str(e))
    