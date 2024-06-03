import flask_login
from .settings import shop
from registration_page.models import User

shop.secret_key = "SECRET_KEY123"
login_maneger = flask_login.LoginManager(app = shop)

@login_maneger.user_loader
def load_user(id):
    return User.query.get(id)
    