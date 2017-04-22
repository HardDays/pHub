from models.bill import *
from helpers.str_generator import *
from controllers.notif_controller import *
from helpers.notification import *
from models.user import *

nc = NotifController(123)

n = Notification('privet petuch')

u = User(1, 'privet petuch', phone='+79991640078')

nc.send_to_user(u, n)