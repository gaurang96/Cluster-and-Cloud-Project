# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:33:09 2020
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

#This file includes a view created in the Location Database to extract the location parameters for Victorian cities.
#Using Map_Reduce functionality, we have been able to achieve desired results. 

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

view = design_document.DesignDocument(my_database,document_id='view')
view.add_view('VIC_data',"""function (doc) {
  if(doc.props.lga_name18=="Melbourne (C)" || doc.props.lga_name=="Melbourne (C)"){
  emit(doc.id, doc);
  }
}""",'_count')
view.save()

import pandas as pd
out=(my_database.get_view_result('_design/VIC_data', 'VIC_data',
    raw_result=True,group=True, group_level=2 ,skip=100))
    
location_list  = []
for i in location['rows']:
    
    location_list.append((i['id'], i['key'][0],i['key'][1], i['value'][0],i['value'][1], i['value'][2]))
    
location_dataframe = pd.DataFrame(location_list, columns=['id', 'longitude','latitude',  'city','state','value'])