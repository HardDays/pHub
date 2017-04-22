class Bill(object):
	def __init__(self, uuid, sender, to, amount):
		self.uuid = uuid
		self.sender = sender
		self.to = to
		self.amount = amount
