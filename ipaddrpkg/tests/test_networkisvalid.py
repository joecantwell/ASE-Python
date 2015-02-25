import pytest
from ipaddrpkg.network import Network 

def test_is_typeof_network():
 	cidr = "192.168/16"	
	network = Network(cidr, "Dummy Address")

	assert network.cidr == cidr
	assert network.type == "network"
