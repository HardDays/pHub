class User(object):
	def __init__(self, uuid, name, contacts=[], phone=None, photo=None):
		self.uuid = uuid
		self.name = name
		self.contacts = contacts
		self.phone = phone
		self.photo = photo

