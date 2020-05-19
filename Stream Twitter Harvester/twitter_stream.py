# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:20:43 2020

@author: Sania Khan
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
    def __init__(self, time_limit=300):
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
            stream = tweepy.Stream(auth = api.auth, listener=streamListener,tweet_mode='extended')
            #tags =['unemployment', 'inflation', 'recession', 'layoff', 'crisis', ' emergency']
            # This line filter Twitter Streams to capture data by the location: 
            stream.filter(locations=gridDetails, languages=['en'])
        except Exception as e:
            print("Error: Restart the stream ", str(e))
    