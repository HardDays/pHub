from db.db_controller import DbController
from models.bill import *
from controllers.transfer_controller import TransferController
from controllers.bill_controller import BillController

class PayForMeController(object):
    db = ""
    transfer_controller =""
    bill_controller = ""

    def __init__(self, db):
        self.db = db
        self.transfer_controller = TransferController(db)
        self.bill_controller = BillController(db)

    def pay_for_me(self, user_id, to, amount, msg):
        potentional_bill = self.bill_controller.send_payment(user_id, to, amount)
        self.db.pre_bill[potentional_bill.to].add(potentional_bill)
        #TODO: !!!send_notif!!!#
        return potentional_bill

    def accept_payment(self, bill_id, user_id):
        bill = self.bill_controller.accept_payment(bill_id, user_id)
        #TODO: !!!send_notif!!!#




