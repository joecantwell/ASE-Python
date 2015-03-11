import data_source

prompt = '> '

valid = ['Y','y','N','n']
while True:
	print """
		Resetting the Network Collection. 
		Do you want to continue (Y/N)?"
		"""
	blowout  = str(raw_input(prompt))
	if blowout in valid:
		if (blowout  == "N" or blowout == "n"):
			print "Leaving Data source as is!"
			break
		else:
			data_source.reset_network_data()
			break
	else:
		print "Invalid input... Try again"
