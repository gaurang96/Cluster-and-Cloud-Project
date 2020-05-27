# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:34:17 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

#Twitter Data map Reduce functions
# 3 Views were created for the tweets using 3 different functions MapReduce functions which are given below.

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant import design_document
serviceUsername = "admin"
servicePassword = "123"
serviceURL = "http://admin:123@172.26.132.96:5984/"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
my_database = client['twitterdata']

#----------------------------------------------------

view = design_document.DesignDocument(my_database,document_id='view')
ddoc.add_view('myview',"""function (doc) {
  if (doc.sentiment.compound > 0.05){
  emit([doc.sentiment.compound, doc.location], 1);
}
}""")
view.save()

#----------------------------------------------------

view2 = design_document.DesignDocument(my_database,document_id='view2')
view2.add_view('view2',"""function (doc) {
  if (doc.sentiment.compound < -0.05){
  emit([doc.sentiment.compound, doc.location], 1);
}
}""")
view2.save()

#----------------------------------------------------

view3 = design_document.DesignDocument(my_database,document_id='view3')
view3.add_view('view3',"""function (doc) {
  if (doc.sentiment.compound > -0.05 && doc.sentiment.compound < 0.05){
  emit([doc.sentiment.compound, doc.location], 1);
}
}""")
view3.save()

#----------------------------------------------------