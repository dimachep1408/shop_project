import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from admin_app.models import Product
from project.settings import DATABASE
import flask_login

def render_shop():
    global product
    


    name = str(flask_login.current_user).split(":")[1]




    return flask.render_template(template_name_or_list= "shop.html", log = name, products = Product.query.all())

def new_func():
    print(f"Test: {User.query.get(True)}")