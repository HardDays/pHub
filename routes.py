"""
Routes and views for the bottle application.
"""

from bottle import route, view, post, request, response, 
from datetime import datetime
import json

from db.db_controller import DbController
from controllers.pay_for_me_controller import PayForMeController
from controllers.content_controller import ContentController
from controllers.bill_controller import BillController

from controllers.notif_controller import NotifController

db = DbController()
pay_for_me = PayForMeController(db)
content = ContentController(db)
notif = NotifController()

@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description papge.',
        year=datetime.now().year
    )

@route('/notifications/send_to_number', method='POST')
def send_to_number():
    notif.send_to_phone(request.forms.get('phone'), request.forms.get('message'))

    #print(request.body.readlines())

@route("/pay_for_me/<user_id>/<to>/<amont>")
def pay_for_me(user_id, to, amount):
    msg = "Pay instead my, please!"
    pay_for_me.pay_for_me(user_id, to, amount, msg)

@route("/users/get_all_users")
def get_all_users():
    return dict(data = db.users)

@route("/pay_for_me/accept_payment/<bill_id>/<user_id>")
def accept_payment(bill_id, user_id):
    return pay_for_me.accept_payment(bill_id, user_id)

@route("bill/get_all_askers/<user_id>")
def get_all_askers(user_id):
    bill_controller.get_all_asks(user_id)