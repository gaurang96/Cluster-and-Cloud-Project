# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:13:47 2020

@author: Sania Khan
"""
from Grid_details import gridDetails
import twitter_stream
import historic_tweets
import data_scheduler
from multiprocessing import Process
import User 
import time
import threading

parallelProcess = []
  
def get_stream_data():
    twitter_account = len(gridDetails)
    print("Gettig stream data")
    # index is the number of keys stores in Grid_details.py 
    # place all the team members key here  
    for index in range(twitter_account):
            twitter_credentials = {
                "ACCESS_TOKEN": gridDetails[index]["ACCESS_TOKEN"],
                "ACCESS_TOKEN_SECRET": gridDetails[index]["ACCESS_TOKEN_SECRET"],
                "CONSUMER_KEY": gridDetails[index]["CONSUMER_KEY"],
                "CONSUMER_SECRET": gridDetails[index]["CONSUMER_SECRET"]
            }
            print("Inside stream")
            twitter_stream.start_stream(twitter_credentials, gridDetails[index]["GRID"])
 
def get_user_data():
    twitter_account = len(gridDetails)
    print("Gettig user data")
    # index is the number of keys stores in Grid_details.py 
    # place all the team members key here  
    for index in range(twitter_account):
        twitter_credentials = {
                    "ACCESS_TOKEN": gridDetails[index]["ACCESS_TOKEN"],
                    "ACCESS_TOKEN_SECRET": gridDetails[index]["ACCESS_TOKEN_SECRET"],
                    "CONSUMER_KEY": gridDetails[index]["CONSUMER_KEY"],
                    "CONSUMER_SECRET": gridDetails[index]["CONSUMER_SECRET"]
                }
        print("Wait for streaming")
        User.getUserList(twitter_credentials)   
    
def get_historic_data():
    historic_tweets.get_historic_tweets()
    
def start_process_data():   
    data_scheduler.start_scheduler()
    
if __name__ == '__main__':
    p1= Process(target=get_stream_data)
    p2 = Process(target=get_user_data)
    p3 = Process(target=get_historic_data)
    p4 = Process(target=start_process_data)
    p1.start()
    time.sleep(300)
    p2.start()
    p3.start()
    time.sleep(100)
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    