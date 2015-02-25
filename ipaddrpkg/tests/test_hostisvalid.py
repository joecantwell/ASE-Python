import pytest
from ipaddrpkg.host import Host
from ipaddrpkg.ipv4 import Ipv4

def test_is_typeof_host():
	ip = Ipv4(192,168,1,254)
 	host = Host(ip, "Dummy Address")

	assert host.type == "host"
	assert host.ip == ip
