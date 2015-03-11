#!/usr/bin/python

class Ipv4(object):

	def __init__(self, ip):
		self.ipv4 = ip
		self.cidr = "{0}/32".format(ip)

	def __init__(self, part1, part2=0, part3=0, part4=0):
		self.ipv4 = "{0}.{1}.{2}.{3}".format(part1, part2, part3, part4)
		self.cidr = self.ipv4 + "/32"

