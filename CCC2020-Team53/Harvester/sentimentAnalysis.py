# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:03:37 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(text):
    # polarity >= 0.05 positive sentiment and polarity<=-0.05 negative sentiment
    score = analyzer.polarity_scores(text)
    return score