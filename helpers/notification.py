class Notification(object):
	def __init__(self, message):
		self.message = message

class BillNotification(Notification):
	def __init__(self, bill, message):
		super(message)
		self.bill = bill

