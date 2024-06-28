import flask
from registration_page.models import User
from login_page.views import log
from admin_app.models import Product
import flask_login

def render_basket():
    

    name = str(flask_login.current_user).split(":")[1]
    print(name)
    
    if flask.request.method == "POST":
        return flask.redirect("/basket/order/")

    return flask.render_template(template_name_or_list= "basket.html", log = name, products = Product.query.all())