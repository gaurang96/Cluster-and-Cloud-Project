
# coding: utf-8

# In[ ]:


import tweepy
import json
import couchdb
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
class Condenser_Tweets:
    def __init__(self, tweet):
        
        self.created_at = tweet["created_at"]
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
        if "text" in tweet:
                return tweet["text"]
        else:
             return ""
    
    def updateOpinion(self, tweetText):
        

        analyzer = SentimentIntensityAnalyzer()
        def sentiment_analyzer_scores(text):
            score = analyzer.polarity_scores(text)
            return score
        scoredData = sentiment_analyzer_scores(tweetText)
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

consumer_key = 'ElbpAhII5t9dDt4w964jMRIGd'
consumer_secret = 'K6MMr2t5ORimg8uivcIdOUoFKygECvGRLpD3yoiuWipAFuuNvb'
access_token = '966495718813782016-P8pxuFvfmtIa5J31IKtGZf8Kykuvjke'
access_secret = 'ws5GehufYcFPNkzekQrdD5zFBjjE34WHPaQGOhPIUceMw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

 
# Connecting with couchdb Server   
couch = couchdb.Server("http://admin:123@172.26.132.96:5984/")  

db = couch.create('twitter_time_series')  
db = couch['twitter_time_series']



htags=['#Unemployment','#auspol']

for search in htags:
    
    for tweet in tweepy.Cursor(api.search,q=search,geocode="-33.865143,151.209900,300km",
                               lang="en",
                               since="2020-01-01").items():
        
        
        try:

            t = (Condenser_Tweets(tweet._json).updatedJson())
            print(t)

            db.save(json.loads(json.dumps(t)))
        except Exception as e:
            print(e)


# In[19]:


get_ipython().system('pip install couchdb')

