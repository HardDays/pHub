class Notification(object):
	def __init__(self, message):
		self.message = message

	def form(self):
		return self.message
