class Group(object):
	def __init__(self, uuid, users=[], bills=[]):
		self.uuid = uuid
		self.users = users
		self.bills = bills