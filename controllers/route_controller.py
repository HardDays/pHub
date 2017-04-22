from helpers.notification import *

class RouteController(object):
	def __init__(self, notif_controller):
		self.notif_controller = notif_controller

	def ask_for_help(self, user, amount):
		nt = Notification('I am {} and asking for help! Give me {} of money, please!'.format(user.name, amount))
		self.notif_controller.send_to_contacts(user, nt)