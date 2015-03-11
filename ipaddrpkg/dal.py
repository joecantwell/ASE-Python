import data_source

class Dal(object):

	def __init__(self):
		self.networks = data_source.loadNetworkData() 
		self.hosts = data_source.loadHostData()
		self.networkFile = 'network.json'
		self.hostFile = 'networkip.json'

	def addNetwork(self, network):
		self.networks.append(network)

	def addHost(self, host):
		self.hosts.append(host)

	def searchNetworks(self, value):
		for network in self.networks:
			for k,v in network.items():
				if value in v:
					return network	

	def searchHosts(self, target):
		found = []
		for host in self.hosts:
			if isinstance(host, dict):
				for key, value in host.iteritems():
					if isinstance(value, dict):
						if target == value['ipv4']:
							found.append(host)
						elif self.search(target,value['cidr']):
							found.append(host)
		return found 

	# perform a partial search 
	def search(self, target, value):
		if target == value:
			return True
		else:
			partial = target.split("/")
			if len(partial) == 2:
				iplen = len(partial[0])
				staticLength = int(partial[1])
				if partial[0] == value[:iplen]:
					#print value[:iplen]
					return True
		return False

	# wriet the changes back to file
	def save(self):
		data_source.write_to_file(self.hostFile, 'w', self.hosts)
		data_source.write_to_file(self.networkFile, 'w', self.networks)
