# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:10:58 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import sentimentAnalysis

class Condenser_Tweets:
    def __init__(self, tweet):
        self.created_at = self.tweetcreatedAt(tweet)
        self._id = self.addID(tweet)
        self.text = self.addText(tweet)
        self.sentiment = self.updateOpinion(self.text)
        self.location = self.updateLocation(tweet)
        
    def updatedJson(self):
        return {
            "_id": self._id,
            "text": self.text,
            "sentiment": self.sentiment,
            "location": self.location,
            "created_at":self.created_at
            }

    def getText(self, tweet):
        return self.text
    
    def addID(self, tweet):
        if ("id" in tweet) and (type(tweet["id"]) == int or type(tweet["id"]) == str):
            return str(tweet["id"])
        else:
            return -1
        
    def addText(self, tweet):
        if ("doc" in tweet) and (type(tweet["doc"]) == dict):
            if ("text" in tweet["doc"] and (type(tweet["doc"]["text"]) == str)):
                return tweet["doc"]["text"]
        else:
            if ("text" in tweet and (type(tweet["text"]) == str)):
                return tweet["text"]
            elif ("full_text" in tweet and (type(tweet["full_text"]) == str)):
                return tweet["full_text"]
        return ""
    
    def updateOpinion(self, tweetText):
        scoredData = sentimentAnalysis.sentiment_analyzer_scores(tweetText)
        return scoredData


    def getTweetCoordinate(self, tweet):
        tweetCoordinates = []
        if ("doc" in tweet) and (type(tweet["doc"]) == dict):         
            if ("coordinates" in tweet["doc"] and (type(tweet["doc"]["coordinates"]) == dict)):
                if ("coordinates" in tweet["doc"]["coordinates"] and (type(tweet["doc"]["coordinates"]["coordinates"]) == list)):
                    tweetCoordinates = tweet["doc"]["coordinates"]["coordinates"]
                    if len(tweetCoordinates) == 2:
                        xCoordinate = tweetCoordinates[0]
                        yCoordinate = tweetCoordinates[1]
                        return [xCoordinate, yCoordinate]
        else:             
            if ("coordinates" in tweet and (type(tweet["coordinates"]) == dict)):
                if ((type(tweet["coordinates"]["coordinates"]) == list) and "coordinates" in tweet["coordinates"]):
                    tweetCoordinates = tweet["coordinates"]["coordinates"]
                    if len(tweetCoordinates) == 2:
                        xCoordinate = tweetCoordinates[0]
                        yCoordinate = tweetCoordinates[1]
                        return [xCoordinate, yCoordinate]
                    
        if ("doc" in tweet) and (type(tweet["doc"]) == dict):
            if ("geo" in tweet["doc"] and (type(tweet["doc"]["geo"]) == dict)):
                if ("coordinates" in tweet["doc"]["geo"] and (type(tweet["doc"]["geo"]["coordinates"]) == list)):
                    tweetCoordinates = tweet["doc"]["geo"]["coordinates"]
                    if len(tweetCoordinates) == 2:
                        xCoordinate = tweetCoordinates[1]
                        yCoordinate = tweetCoordinates[0]
                        return [xCoordinate, yCoordinate]
        else:
            if ("geo" in tweet and (type(tweet["geo"]) == dict)):
                if ((type(tweet["geo"]["coordinates"]) == list) and"coordinates" in tweet["geo"]):
                    tweetCoordinates = tweet["geo"]["coordinates"]
                    if len(tweetCoordinates) == 2:
                        xCoordinate = tweetCoordinates[1]
                        yCoordinate = tweetCoordinates[0]
                        return [xCoordinate, yCoordinate]
                    
        if ("value" in tweet) and (type(tweet["value"]) == dict): 
            if ("geometry" in tweet["value"] and (type(tweet["value"]["geometry"]) == dict)):
                if ("coordinates" in tweet["value"]["geometry"] and (type(tweet["value"]["geometry"]["coordinates"]) == list)):
                    tweetCoordinates = tweet["value"]["geometry"]["coordinates"]
                    if len(tweetCoordinates) == 2:
                        xCoordinate = tweetCoordinates[0]
                        yCoordinate = tweetCoordinates[1]
                        return [xCoordinate, yCoordinate]    
                    
        return [-1, -1]
   
    def updateLocation(self, tweetjson):
        return self.getTweetCoordinate(tweetjson)
    
    
    def tweetcreatedAt(self, tweet):
        if ("doc" in tweet) and (type(tweet["doc"]) == dict):
            if ("created_at" in tweet["doc"] and (type(tweet["doc"]["created_at"]) == str)):
                return tweet["doc"]["created_at"]
        