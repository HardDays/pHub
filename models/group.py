from helpers.str_generator import *

class Group(object):

	uuid = ""
	users = []
	bills = []

	def __init__(self, users=[], bills=[]):
		self.uuid = str_gen()
		self.users = users
		self.bills = bills