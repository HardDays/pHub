from db.db_controller import DbController
from models.user import User


class ContentController(object):
    db = ""

    def __init__(self, db):
        self.db = db

        users = self.genUsers()
        self.db.users = users


    def genUsers(self):
        user1 = User( "Vlad", [], "+79991640078", None, stat = 85)
        user2 = User( "Vova", [], "+79991640078", None, stat =92)
        user3 = User( "Maria", [], "+79991640078", None, stat = 90)
        users = list()
        users.append(user1)
        users.append(user2)
        users.append(user3)

        return users