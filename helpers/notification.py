class Notification(object):
	def __init__(self, message):
		self.message = message

	def form(self):
		return self.message

class BillNotification(Notification):
	def __init__(self, bill, message):
		super(message)
		self.bill = bill

	def form(self):
		return 'Transfer from' + self.bill.sender.name + 'Amount: ' + str(self.bill.amount) + ' ' + self.message

