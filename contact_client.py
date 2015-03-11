import addressbook_pb2
import sys

prompt = '> '

def addContact():
	contact = addressbook_pb2.Contact()
	contact.name = raw_input("Enter Name: ")
	contact.id = int(raw_input("Enter Id Number: "))
	contact.email = raw_input("Enter Email: ")	
	with addressbook_pb2.early_adopter_create_ContactService_stub('localhost', 50052) as stub:
		response = stub.AddContact(contact, 10)
		print response.msg

while True:
	print """
	What do you want to do?
	A - add a contact
	S - query a contact
	Q - quit
	"""
	action = str(raw_input(prompt))
	if (action == 'A' or action == 'a'):
		addContact()
	else:
		break

