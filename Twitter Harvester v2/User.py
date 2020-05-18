# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:22:17 2020

@author: Sania Khan
"""
import tweepy
import json
from pathlib import Path
from datetime import datetime 
Path('user_list_timeline.json').touch()
def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()


def get_userid(line, ):
    line = line.rpartition("}")[0] + "}"
    if len(line) > 0:
        data = json.loads(line)
        uid = data["user"]["id"]
        return uid


def getUserList(twitter_credentials):
        v1 = 'recent_tweets.json'
        v2 = 'user_list_timeline.json'
        # Processing authentication
        auth = tweepy.OAuthHandler(twitter_credentials["CONSUMER_KEY"], twitter_credentials["CONSUMER_SECRET"])
        auth.set_access_token(twitter_credentials["ACCESS_TOKEN"], twitter_credentials["ACCESS_TOKEN_SECRET"])

        # Create interface
        api = tweepy.API(auth, wait_on_rate_limit=True)
        users = []
        with open(v1) as f:
            for line in f:
                try:
                    uid = get_userid(line)
                    if uid not in users:
                        users.append(uid)
                        for tweet in tweepy.Cursor(api.user_timeline, id=uid).items():
                            data = tweet._json
                            if data["coordinates"] is not None:
                                write_file(v2, data)
                except ValueError:
                    continue
                except:
                    continue