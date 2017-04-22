class DbController(object):
	def __init__(self):
		self.users = {}
		self.bills = {}
		self.tokens = {}
		self.groups = {}
		self.group_bills = {}