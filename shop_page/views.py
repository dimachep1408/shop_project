import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from admin_app.models import Product
from project.settings import DATABASE

def render_shop():
    global product
    


    name =f" {flask.session.get('log')}"


    # users = User.query.filter_by(is_admin = True).all()
    
    # nicknames = []

    # print(users)

    # for user in users:
    #     nicknames.append(str(user).split(":")[1])

    # for nickname in nicknames:
    #     if nickname == name:
    #         return flask.redirect("/admin/")









    return flask.render_template(template_name_or_list= "shop.html", log = name, products = Product.query.all())

def new_func():
    print(f"Test: {User.query.get(True)}")