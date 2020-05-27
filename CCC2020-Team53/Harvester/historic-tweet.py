# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:03:37 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import couch_db
import os
import json
from Condenser import Condenser_Tweets
from pathlib import Path

def write_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()
    
def removeFile(fullFilePath):
    os.remove(fullFilePath)

def get_historic_condensed():
    Path('historic_dbdata.json').touch()
    v2 = 'historic_dbdata.json'
    with open ('twitter-melb.json', 'r+', encoding='utf8') as tweetFile:
            for lineNum,line in enumerate(tweetFile):
                if lineNum > 355000:
                    if str(line[-2]) == ',':
                        tweetDetails = json.loads(line[:-2])
                        search_condenser = Condenser_Tweets(tweetDetails)
                        if search_condenser.text == '' or search_condenser.location[0] == -1 or search_condenser.location[1] == -1:
                            continue
                        else:
                            data = search_condenser.updatedJson()
                            write_file(v2, data) 

if __name__ == '__main__':
    get_historic_condensed()
    couch_db.add_to_DB("historic_dbdata.json")