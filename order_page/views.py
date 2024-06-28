import flask
from registration_page.models import User
from login_page.views import log
from admin_app.models import Product
from project.mail_config import mail, ADMINISTRATOR_ADDRESS
from flask_mail import Message
import flask_login


def render_order():

    gmail = flask.request.form.get("inputEmailModal")
    

    name = str(flask_login.current_user).split(":")[1]



    if flask.request.method == "POST":
        
        message = Message(
            "Message Order",
            sender = ADMINISTRATOR_ADDRESS,
            recipients= ["dmitriychep2011@gmail.com"],
            body = "Your order was send"
        )

        mail.send(message)
        print("work")
    return flask.render_template(template_name_or_list= "order.html", log = name, products = Product.query.all())