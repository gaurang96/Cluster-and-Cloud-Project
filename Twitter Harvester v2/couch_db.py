# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:48:24 2020

@author: Sania Khan
"""

import couchdb
import json

def initConnection():
    couch_connection = couchdb.Server('http://admin:admin123@172.0.0.1:5984/')
    database_name = 'twitterdata1'
    print("Connected")
    if database_name in couch_connection:
        print("Data Base already exists")
        db = couch_connection[database_name]
    else:
        print("Create database")
        db = couch_connection.create(database_name)
        print("Connected to Database")
    return db

def add_to_DB(filePath):
    couch_connection = couchdb.Server('http://admin:admin123@172.0.0.1:5984/')
    print("Connected")
    database_name = 'twitterdata1'
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
                #data = line.replace('\'', '"')            
                filedata = json.loads((line))
                if filedata["_id"] in db:
                    print("Doc exists already")
                else:
                    db.save(filedata)
            except Exception as e:
                print("Error while updating document to the database",str(e))

    