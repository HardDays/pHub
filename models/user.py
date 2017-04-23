from helpers.str_generator import *

class User(object):

	uuid = ""
	name = ""
	contacts = ""
	phone = ""
	photo = ""
	stat = ""

	def __init__(self, name, contacts=[], phone=None, photo=None, stat = 100):
		self.uuid = str_gen()
		self.name = name
		self.contacts = contacts
		self.phone = phone
		self.photo = photo
		self.stat = stat

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)

