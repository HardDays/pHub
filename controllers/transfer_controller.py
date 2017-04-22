from helpers.str_generator import *

class TransferController(object):
	def __init__(self, db_collector):
		self.db_collector = db_collector

	def transfer(self, sender, to, amount):
		bill = Bill(str_gen(), sender, to, amount)
		self.db_collector.bills[bill.id] = bill

	