# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:29:16 2020

@author: Sania Khan
"""

import process_data
import time

def start_scheduler():
    print("Starting scheduler")
    time.sleep(600)
    process_data.getTweets_condensed()
    process_data.process_tweet_data()
    process_data.get_historic_condensed()
