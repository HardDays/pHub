from helpers.str_generator import *

class TransferController(object):

	def __init__(self, db_controller):
		self.db_controller = db_controller

	def transfer(self, sender, to, amount):
		bill = Bill(sender, to, amount)
		self.db_controller.bills[sender].add(bill)
		return bill

	def group_transfer(self, user, amount, group_id):
		bill = GroupBill(user, amount, group_id)
		self.db_controller.groups[group_id].bills.add(bill)


	def init_transfer(self, sender, to, amount):
		bill = Bill(str_gen(), sender, to, amount)
		return bill

	def commit_transfer(self, bill):
		self.db_controller.bills[sender].add(bill)


	