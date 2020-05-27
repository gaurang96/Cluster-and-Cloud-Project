# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:29:16 2020

Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import process_data

def start_scheduler():
    print("Starting scheduler")
    # Condensed stream tweets
    process_data.getTweets_condensed()
    process_data.process_tweet_data()
    #process_data.get_historic_condensed()
