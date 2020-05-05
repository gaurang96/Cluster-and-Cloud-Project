# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:13:47 2020

@author: Sania Khan
"""
from Grid_details import gridDetails
import twitter_stream

twitter_account = len(gridDetails)
# index is the number of keys stores in Grid_details.py 
# place all the team members key here  
for index in range(twitter_account):
        twitter_credentials = {
            "ACCESS_TOKEN": gridDetails[index]["ACCESS_TOKEN"],
            "ACCESS_TOKEN_SECRET": gridDetails[index]["ACCESS_TOKEN_SECRET"],
            "CONSUMER_KEY": gridDetails[index]["CONSUMER_KEY"],
            "CONSUMER_SECRET": gridDetails[index]["CONSUMER_SECRET"]
        }
        print("File with index number " + str(index))
        twitter_stream.start_stream(twitter_credentials, gridDetails[index]["GRID"])
      