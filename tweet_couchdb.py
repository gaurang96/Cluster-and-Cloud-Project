import tweepy
import json
import couchdb

consumer_key = 'ElbpAhII5t9dDt4w964jMRIGd'
consumer_secret = 'K6MMr2t5ORimg8uivcIdOUoFKygECvGRLpD3yoiuWipAFuuNvb'
access_token = '966495718813782016-P8pxuFvfmtIa5J31IKtGZf8Kykuvjke'
access_secret = 'ws5GehufYcFPNkzekQrdD5zFBjjE34WHPaQGOhPIUceMw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

 
# Connecting with couchdb Server   
couch = couchdb.Server("http://user:123@172.26.132.80:5984/")  

#db = couch.create('mydatabase')  
db = couch['mydatabase']



htags=['#Unemployment','#auspol']

for search in htags:
    
    for tweet in tweepy.Cursor(api.search,q=search,geocode="-33.865143,151.209900,1000km",
                           lang="en",
                           since="2020-01-01").items():

        db.save(json.loads(json.dumps(tweet._json)))

