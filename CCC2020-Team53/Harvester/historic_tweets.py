# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:33:23 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import requests
import couch_db
import os
import time
from multiprocessing import Process
from pathlib import Path
import process_data

def removeFile(fullFilePath):
    os.remove(fullFilePath)

def get_historic_tweets_201801():
  Path('melb.json').touch()
  fileOpen_1 = 'melb.json'
  print("Inside here")
  url = 'http://readonly:ween7ighai9gahR6@45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary?include_docs=true&reduce=false&start_key=["melbourne",2018,1,1]&end_key=["melbourne",2018,1,31]'
  response = requests.get(url, stream=True)
  write_file_1 = open(fileOpen_1, "wb")
  for data_chunk in response.iter_content(chunk_size=512):     
    if data_chunk:  
      write_file_1.write(data_chunk)
  write_file_1.close()

if __name__ == '__main__':
    p1= Process(target=get_historic_tweets_201801())
    p1.start()
    time.sleep(60)
    p1.terminate()    
    process_data.get_historic_condensed()
    print("here")
    couch_db.add_to_DB("historic_dbdata.json")
    removeFile("historic_dbdata.json")
    removeFile("melb_2018.json")
  