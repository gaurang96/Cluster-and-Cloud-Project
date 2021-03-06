# -*- coding: utf-8 -*-
"""
Team 53
Melbourne
@author: Sania Khan(1045290), Kanav Sood(1057606), Gaurang Sharma(1041953), Udit Goel(1042890), Jack Crellin(1168062)
"""

import cloudant

class database:
	def __init__(self, ip, user, pw):
		self.ip = ip
		self.client = cloudant.client.Cloudant(user, pw, url="http://{}:{}@{}".format(user, pw, self.ip))

	def connect(self):
		self.client.connect()
		print("client connected")

	# returns the data stored as a result of a view query
	def collect_data(self, idx):
		key = self.client['ui_input'].keys(remote=True)[idx]

		return (self.client['ui_input'][key])


	def disconnect(self):
		self.client.disconnect()