from helpers.link_former import *
from db.db_controller import DbController
from models.bill import *
from transfer_controller import TransferController
from bill_controller import BillController
from request_pay_controller import RequestPayController
from helpers.notification_former import NotificaitonFormer
from notifcontroller import NotifController

class RequestPayController(object):
    db = None
    transfer_controller = None
    bill_controller = None

    def __init__(self, db):
        self.db = db
        self.transfer_controller = TransferController(db)
        self.bill_controller = BillController(db)
        self.notification_former = NotificaitonFormer()
        self.notif_controller = NotifController()

    def ask_payment(self, sender, amount, msg):
        potentional_bill = self.bill_controller.send_payment(None, to, amount)
        self.db.pre_bill[potentional_bill.to].add(potentional_bill)
        
        notif = self.notification_former.form_request_pay(potentional_bill, form_link('pay/' + potentional_bill.uuid))
        self.notif_controller.send_to_contacts(notif)

        return potentional_bill

    def accept_payment(self, sender, to, bill_id):
        bill = self.db_controller.getUserPreBillById(to, bill_id)
        bill.sender = sender
        bill = self.bill_controller.accept_payment(bill_id, to)
        
        notif = self.notification_former.form_bill(bill, 'SUCCSESS')

        self.notif_controller.send_to_user(bill.to, notif)
        self.notif_controller.send_to_user(bill.sender, notif)




