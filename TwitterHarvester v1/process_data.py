# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:47:49 2020

@author: Sania Khan
"""

import json
from Condenser import Condenser_Tweets

def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()
v2 = "process_tweets_db.json" 
   
if __name__ == "__main__":
    with open ('recent_tweets.json', 'r+', encoding='utf8') as tweet_handle:
                for data_item in tweet_handle:
                    tweetDetails = json.loads(data_item)
                    stream_condenser = Condenser_Tweets(tweetDetails)
                    data = stream_condenser.updatedJson()
                    with open(v2) as f:
                      write_file(v2, data)  
                      
                      
    with open ('user_list_timeline.json', 'r+', encoding='utf8') as tweet_handle:
            for data_item in tweet_handle:
                tweetDetails = json.loads(data_item)
                search_condenser = Condenser_Tweets(tweetDetails)
                data = search_condenser.updatedJson()
                with open(v2) as f:
                      write_file(v2, data)  