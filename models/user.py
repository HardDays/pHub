class User(object):
	def __init__(self, uuid, name, contacts=[], phone='', photo=''):
		self.uuid = uuid
		self.name = name
		self.contacts = contacts
		self.phone = phone
		self.photo = photo

