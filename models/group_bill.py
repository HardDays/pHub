from helpers.str_generator import *

class GroupBill(object):

	uuid = ""
	user = ""
	amount = ""
	group_id = ""

	def __init__(self, user, amount, group_id):
		self.uuid = str_gen()
		self.user = user
		self.amount = amount
		self.group_id = group_id