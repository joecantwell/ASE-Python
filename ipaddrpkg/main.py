from network import Network
from host import Host
from ipv4 import Ipv4
from dal import Dal

prompt = '> '

def addNetwork():
	print "Enter Network"
	cidr = str(raw_input(prompt))

	print "Enter Network Note/Info"
	note = str(raw_input(prompt))

	net = Network(cidr, note)
	dal = Dal()
	dal.addNetwork(net)
	dal.save()

def addHost():
	print "Enter Host Ipv4 Address"
	ipadr = str(raw_input(prompt))

	print "Enter Comment/Note"
	note = str(raw_input(prompt))

	ip4 = buildIp(ipadr)
	host = Host(ip4, note)
	dal = Dal()
	dal.addHost(host)
	dal.save()

def buildIp(ipadr):
	ip = ipadr.split('.')
	if len(ip) == 4:
		ip4 = Ipv4(ip[0], ip[1],ip[2], ip[3])	
	elif len(ip) == 3:
		ip4 = Ipv4(ip[0], ip[1],ip[2])
	elif len(ip) == 2:	
		ip4 = Ipv4(ip[0], ip[1])
	else:
		ip4 = Ipv4(ip[0], ip[1])

	return ip4

def searchNetwork():
	print "Enter CIDR to Search"
	cidr = str(raw_input(prompt))
	dal = Dal()
	searchresults = dal.searchNetworks(cidr)
	if searchresults == None:
		print "Nothing Found..."
	else:
		print searchresults
	print cidr in dal.networks

def searchHost():
	print "Enter IP to Search"
	query = str(raw_input(prompt))
	dal = Dal()
	hostresults = dal.searchHosts(query)
	if hostresults == None:
		print "Nothing Found..."
	else:
		print hostresults

while True:
	print """
	What do you want to do?
	n  - Add a Network (CIDR)
	h  - Add a Host (IP Address)
	sn - Search for a Network (CIDR)
	sh - Search for a Host (IPv4 or CIDR) 
	q  - Quit
	"""
	valid = ['n','h','N','H','sn','SN','sh','SH','q','Q']
	action = str(raw_input(prompt))
	if action in valid:
		if (action == 'n' or action == 'N'):
			addNetwork()
		elif(action == 'h' or action == 'H'):
			addHost()
		elif(action == 'sn' or action == 'SN'):
			searchNetwork()
		elif(action == 'sh' or action == 'SH'):
			searchHost()
		else:
			break
	else:
		print "Invalid input... try again"
