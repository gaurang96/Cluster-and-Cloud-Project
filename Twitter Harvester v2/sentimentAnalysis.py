# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:03:37 2020

@author: Sania Khan
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    return score