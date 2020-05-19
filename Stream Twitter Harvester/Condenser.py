# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:10:58 2020

@author: Sania Khan
"""

import sentimentAnalysis

class Condenser_Tweets:
    def __init__(self, tweet):
        self._id = self.addID(tweet)
        self.text = self.addText(tweet)
        self.sentiment = self.updateOpinion(self.text)
        self.location = self.updateLocation(tweet)
    def updatedJson(self):
        return {
            "_id": self._id,
            "text": self.text,
            "sentiment": self.sentiment,
            "location": self.location
            }

    def getText(self, tweet):
        return self.text
    
    def addID(self, tweet):
        if ("id" in tweet) and (type(tweet["id"]) == int or type(tweet["id"]) == str):
            return str(tweet["id"])
        else:
            return -1
        
    def addText(self, tweet):
        if "text" in tweet:
                return tweet["text"]
        else:
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
        return [-1, -1]

   
    def updateLocation(self, tweetjson):
        return self.getTweetCoordinate(tweetjson)
    
    

        