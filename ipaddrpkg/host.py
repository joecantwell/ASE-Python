#!/usr/bin/python

class Host(object):

	def __init__(self, ip, note = "Unknown Device"):
		self.ip = ip
		self.note = note
		self.type = "host"

