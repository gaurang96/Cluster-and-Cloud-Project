# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:29:16 2020

@author: Sania Khan
"""

import process_data

def start_scheduler():
    print("Starting scheduler")
    process_data.getTweets_condensed()
    process_data.process_tweet_data()
    #process_data.get_historic_condensed()
