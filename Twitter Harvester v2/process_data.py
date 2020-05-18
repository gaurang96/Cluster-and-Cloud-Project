# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:47:49 2020

@author: Sania Khan
"""

import json
import os
from Condenser import Condenser_Tweets
import couch_db
from pathlib import Path
Path('historic_dbdata.json').touch()
Path('user_tweets_db.json').touch()
Path('process_tweets_db.json').touch()
def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()
    
def removeFile(fullFilePath):
    os.remove(fullFilePath)
   
def getTweets_condensed():      
    v2 = "process_tweets_db.json" 
    with open ('recent_tweets.json', 'r+', encoding='utf8') as tweet_handle:
                for data_item in tweet_handle:
                    tweetDetails = json.loads(data_item)
                    stream_condenser = Condenser_Tweets(tweetDetails)
                    data = stream_condenser.updatedJson()
                    write_file(v2, data)
                    print("Stream processed with Stream")
                      
    v3 ="user_tweets_db.json"                  
    with open ('user_list_timeline.json', 'r+', encoding='utf8') as tweet_handle:
            for data_item in tweet_handle:
                tweetDetails = json.loads(data_item)
                search_condenser = Condenser_Tweets(tweetDetails)
                data = search_condenser.updatedJson()
                write_file(v3, data) 
                print("Search processed tweets for database")
        
def get_historic_condensed():
    v2 = "historic_dbdata.json"
    with open ('1_2018.json', 'r+', encoding='utf8') as tweetFile:
            for lineNum, line in enumerate(tweetFile):
                    if lineNum > 0:
                        if "coordinates" in str(line):
                            if str(line[-2]) == ',':
                                line = line[:-2]
                            elif str(line[-3:-1]) == "]}":
                                break
                            tweetDetails = json.loads(line)
                            search_condenser = Condenser_Tweets(tweetDetails)
                            data = search_condenser.updatedJson()
                            write_file(v2, data) 

def process_tweet_data():
    try:
        couch_db.add_to_DB("process_tweets_db.json")
        couch_db.add_to_DB("user_tweets_db.json")
        couch_db.add_to_DB("historic_dbdata.json")
        removeFile("process_tweets_db.json")
        removeFile("historic_dbdata.json")
        removeFile("user_tweets_db.json")
        removeFile("process_tweets_db.json")
        removeFile("user_tweets_db.json")
        removeFile("historic_dbdata.json")

    except Exception as e:
        print("Error occurred while processing")
        print(str(e))