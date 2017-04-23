

class DbController(object):

	users = ""
	bills= ""
	tokens= ""
	groups= ""
	group_bills= ""
	pay_for_me= ""
	

	def __init__(self):
		self.users = {}

		#map ordered by user
		self.bills = {}

		self.tokens = {}
		self.groups = {}
		self.group_bills = {}

		#map ordered by 'to' user
		self.pre_bills = {}

	
	def getUserPreBillById(self, user_id, bill_id):
		user_bills = self.pre_bills[user_id]

		for i in user_bills:
			if (i.id == bill_id):
				return i

	def getAllUserBills(self, user_id):
		return self.bills[user_id]