from twilio.rest import Client

class NotifController(object):
	def __init__(self, db_collector):
		self.db_collector = db_collector
		self.client = Client('SKaeabc58042634cd32b65c545ff4cb42b', 'Q6Y2g5mEiZMAYAl3kBSPPA6BvhaSfn2F', 'ACd8d6b302b4c2443c0d5c4900c83be654')

	def send_to_user(self, user, notification):
		if user.phone:
			message = self.client.api.account.messages.create(to=user.phone,
                                             from_='+12029993558',
                                             body=notification.form())

	def send_to_group(self, group, notification):
		for user in group.users:
			self.sent_to_user(user, notification)
