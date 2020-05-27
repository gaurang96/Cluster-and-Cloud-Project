# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:47:49 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import json
import os
from Condenser import Condenser_Tweets
import couch_db
from pathlib import Path

def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()
    
def removeFile(fullFilePath):
    os.remove(fullFilePath)
   
def getTweets_condensed(): 
    Path('process_tweets_db.json').touch()     
    v2 = "process_tweets_db.json" 
    with open ('recent_tweets.json', 'r+', encoding='utf8') as tweet_handle:
                for data_item in tweet_handle:
                    tweetDetails = json.loads(data_item)
                    stream_condenser = Condenser_Tweets(tweetDetails)
                    if stream_condenser.text == '' or stream_condenser.location[0] == -1 or stream_condenser.location[1] == -1:
                        continue
                    else:
                        data = stream_condenser.updatedJson()
                        write_file(v2, data)
                    print("Stream processed with Stream")
                      
        
def get_historic_condensed():
    Path('historic_dbdata.json').touch()
    v2 = 'historic_dbdata.json'
    print("In historic condenser")
    with open ('melb.json', 'r+', encoding='utf8') as tweetFile:
            for lineNum,line in enumerate(tweetFile):
                if lineNum > 200000:
                    if str(line[-2]) == ',':
                        tweetDetails = json.loads(line[:-2])
                        search_condenser = Condenser_Tweets(tweetDetails)
                        if search_condenser.text == '' or search_condenser.location[0] == -1 or search_condenser.location[1] == -1:
                            continue
                        else:
                            data = search_condenser.updatedJson()
                            write_file(v2, data) 
                          
def process_tweet_data():
    try:
        couch_db.add_to_DB("process_tweets_db.json")
        couch_db.add_to_DB("user_tweets_db.json")
        removeFile("recent_tweets.json")
        removeFile("process_tweets_db.json")
        removeFile("user_list_timeline.json")
        removeFile("user_tweets_db.json")

    except Exception as e:
        print("Error occurred while processing")
        print(str(e))