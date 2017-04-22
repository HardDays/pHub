class NotifController(object):
	def __init__(self, db_collector):
		self.db_collector = db_collector

	def sent_to_user(self, user, notification):
		pass

	def send_to_group(self, group, notification):
		for user in group.users:
			self.sent_to_user(user, notification)
