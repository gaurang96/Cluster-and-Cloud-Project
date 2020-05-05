# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:20:43 2020

@author: Sania Khan
"""
import datetime
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

v2 ='recent_tweets.json'
class TwitterStreamer():
    def __init__(self):
        pass

    def crawl_tweets(self,twitter_credentials, bounding_box):
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials["CONSUMER_KEY"], twitter_credentials["CONSUMER_SECRET"])
        auth.set_access_token(twitter_credentials["ACCESS_TOKEN"], twitter_credentials["ACCESS_TOKEN_SECRET"])
        stream = Stream(auth, listener)
        #tags =['unemployment', 'inflation', 'recession', 'layoff', 'crisis', ' emergency']
        # This line filter Twitter Streams to capture data by the location: 
        stream.filter(locations=bounding_box, languages=['en'])

class StdOutListener(StreamListener):
    def __init__(self):
        pass

    def on_data(self, data):
        try:
            write_file(v2,data)
            return True
        except BaseException as e:
            print("Error: %s" % str(e))
        return True
          
    # restriction of max rate limit
    def on_error(self, status_code):
        if status_code == 420:
                self.on_timeout()
    # sleep for 20 minutes
    def on_timeout(self):

            time.sleep(1200)
def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(json.loads(data)) + "\n")
    outfile.close()


def start_stream(credentials, gridDetails):
    while True:
        try:
            twitter_streamer = TwitterStreamer()
            twitter_streamer.crawl_tweets(credentials, gridDetails)
        except Exception as e:
            print("Error: Restart the stream ", str(e))
    