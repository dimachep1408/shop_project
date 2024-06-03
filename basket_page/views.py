import flask
from registration_page.models import User
from login_page.views import log
from admin_app.models import Product


def render_basket():
    

    name = flask.session.get('log')
    print(name)

    return flask.render_template(template_name_or_list= "basket.html", log = name, products = Product.query.all())