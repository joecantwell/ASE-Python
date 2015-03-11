#!/usr/bin/python

class Network(object):

	def __init__(self, cidr, note = "Unknown Subnet"):
		self.cidr = cidr
		self.note = note
		self.type = "network"
