# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:48:24 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import couchdb
import json

def initConnection():
    couch_connection = couchdb.Server('http://admin:123@172.26.132.96:5984/')
    database_name = 'twitter_time_series'
    print("Connected to DB")
    if database_name in couch_connection:
        print("Data Base already exists")
        db = couch_connection[database_name]
    else:
        print("Create database")
        db = couch_connection.create(database_name)
        print("Connected to Database")
    return db

def add_to_DB(filePath):
    couch_connection = couchdb.Server('http://admin:123@172.26.132.96:5984/')
    print("Connected")
    database_name = 'twitter_time_series'
    if database_name in couch_connection:
        print("Data Base already exists")
        db = couch_connection[database_name]
    else:
        print("Data Base does not exist. Creating it")
        db = couch_connection.create(database_name)
        print("Connected to DataBase")
    with open(filePath, 'r+', encoding="utf-8") as tweetHandle:
        for lineNum, line in enumerate(tweetHandle):
            try:          
                filedata = json.loads((line))
                if filedata["_id"] in db:
                    print("Document exists already")
                else:
                    db.save(filedata)
            except Exception as e:
                print("Error while updating document to the database",str(e))

    