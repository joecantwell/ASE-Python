import json
from host import Host
from network import Network
from ipv4 import Ipv4

def reset_network_data():
	print "Resetting data now!"

	networks =[]
	networks.append(Network("192/8"))
	networks.append(Network("192.168/16"))
	
	hosts = []
	for i in range(1, 255):
		#networks.append(Network("192.168.{0}/24".format(i)))
		#for j in range(1, 255):
		ip = Ipv4(192, 168, 1, i) 
		print ip.ipv4
		hosts.append(Host(ip))

	# Store the IP Addresses
	write_to_file('networkip.json', 'w', hosts)	


	# Store the Network CIDR
	write_to_file('network.json', 'w', networks)	



def loadNetworkData():
	networkData = read_from_file('network.json')
	return networkData


def loadHostData():	
	hostData = read_from_file('networkip.json')
	return hostData



def write_to_file(fileName, fileType, collection):
	with open(fileName, fileType) as datafile:
		json.dump(collection, datafile, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def read_from_file(fileName):
	with open(fileName) as datafile:
		data = json.load(datafile)
		return data
