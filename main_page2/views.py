import flask
from registration_page.models import User
from login_page.views import log
import flask_login

def render_main2():

    name = str(flask_login.current_user).split(":")[1]
    print(name)

    return flask.render_template(template_name_or_list= "main2.html", log = name)