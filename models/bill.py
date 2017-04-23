from helpers.str_generator import *

class Bill(object):
	def __init__(self, sender, to, amount):
		self.uuid = str_gen()
		self.sender = sender
		self.to = to
		self.amount = amount
