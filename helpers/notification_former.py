from notification import *

class NotificationFormer(object):
	def __init__(self):
		pass

	def form_bill(self, bill):
		return Notification('Transfer from ' + bill.sender.name + 'Amount: ' + str(bill.amount) + ' ')

	def form_request_pay(self, pot_bill, msg):
		return Notification('I am {} and asking for help! Give me {} of money, please! {}'.format(pot_bill.user.name, pot_bill.amount, msg))
