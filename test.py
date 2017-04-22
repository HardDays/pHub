from models.bill import *
from helpers.str_generator import *
from controllers.notif_controller import *
from helpers.notification import *
from models.user import *

nc = NotifController(123)

n = Notification('Preved')

u = User(1, 'dds', phone='+79991623236')

nc.send_to_user(u, n)