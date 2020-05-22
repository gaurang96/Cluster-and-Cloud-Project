# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:33:23 2020

@author: Sania Khan
"""

import requests
import couch_db
import os
import time
from multiprocessing import Process
from pathlib import Path
import process_data
Path('melb_2018.json').touch()

def removeFile(fullFilePath):
    os.remove(fullFilePath)

def get_historic_tweets_2018():
  fileOpen_1 = 'melb_2018.json'
  print("Inside here")
  url = 'http://readonly:ween7ighai9gahR6@45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary?include_docs=true&reduce=false&start_key=["melbourne",2018,1,1]&end_key=["melbourne",2018,1,31]'
  response = requests.get(url, stream=True)
  write_file_1 = open(fileOpen_1, "wb")
  for data_chunk in response.iter_content(chunk_size=512):     
    if data_chunk:  
      write_file_1.write(data_chunk)
  write_file_1.close()
  
if __name__ == '__main__':
    p1= Process(target=get_historic_tweets_2018)
    p1.start()
    time.sleep(500)
    p1.terminate()    
    process_data.get_historic_condensed()
    couch_db.add_to_DB("historic_dbdata.json")
    removeFile("historic_dbdata.json")
