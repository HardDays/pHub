from transfer_controller import TransferController

from db.db_controller import DbController
from models.group_bill import *
from bill_controller import BillController


class GroupController:
    db = ""
    transfer_controller = ""
    bill_controller = ""

    def __init__(self,db):
        self.db = db
        self.transfer_controller = TransferController(db)
        self.bill_controller = BillController(db)

    def create_group(self, user_id):
        group = Group()
        group.users.add(user_id)
        self.db.group[group.uuid] = group
        return group.uuid

    def add_user_to_group(self, group_id, user_id):
        group = self.db.group[group_id]
        group.users.add(user_id)
        self.db.group[group.uuid] = group

    def add_bill_to_group(self, group_id, user_id, amount):
        self.transfer_controller.group_transfer(user_id, amount, group_id)

    def count_debts(self, group_id):
        #Maria's module
        #result: map{user_id: debt}

    def bill_a_group(self, group_id, user_id):
        debts = self.count_debts(group_id)
        for user, debt in d.iteritems():
            #TODO: send_notif(user, debt)
            bill = self.bill_controller.send_payment(user_id, user, debt*-1)
            self.db.pre_bills[user].add(bill)

    def get_group_bills(self, group_id):
        return self.db.groups[group_id].bills

    def get_group_users(self, group_id):
        group = self.db.groups[group_id].users
        my_users = ()
        for i in group.users:
            my_users.add(self.db.users[i])
        return my_users
