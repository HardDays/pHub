from helpers.notification import *
from controllers.notif_controller import NotifController

class RouteController(object):

	notif_controller = ""
	pay_for_me_controller = ""

	def __init__(self, notif_controller, pay_for_me_controller):
		self.notif_controller = notif_controller
		self.pay_for_me_controller = pay_for_me_controller

	 def ask_for_help(self, user, amount, msg):
	 	nt = Notification('I am {} and asking for help! Give me {} of money, please!'.format(user.name, amount) + msg)
	 	self.notif_controller.send_to_contacts(user, nt)


	

