import flask
from registration_page.models import User
from login_page.views import log

def render_main2():

    name = flask.session.get('log')
    print(name)

    return flask.render_template(template_name_or_list= "main2.html", log = name)