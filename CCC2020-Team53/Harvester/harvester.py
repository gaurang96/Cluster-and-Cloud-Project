# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:13:47 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""
from Grid_details import gridDetails
import twitter_stream
import data_scheduler

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
    
    
def start_process_data():   
    data_scheduler.start_scheduler()
    
if __name__ == '__main__':
  get_stream_data()
  print("Stream data collected")  
  start_process_data()
  print("Stream data stored in dB")