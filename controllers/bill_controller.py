from db.db_controller import DbController
from models.bill import *
from transfer_controller import TransferController


class BillController(object):

    db = ""
    transfer_controller = ""

    def __init__(self, db):
        self.db = db
        self.transfer_controller = TransferController(db)

    def send_payment(self, user_id, to, amount):
        potentional_bill = self.transfer_controller.init_transfer(user_id, to, amount)
        return potentional_bill

    def accept_payment(self, bill_id, user_id):
        bill = self.db.getUserPreBillById(user_id, bill_id)

        self.transfer_controller.commit_transfer(bill)
        return bill

    def get_all_asks(self, user_id):
        return self.db.pre_bill[user_id]