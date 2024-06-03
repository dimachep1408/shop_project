import flask
import flask_login
from registration_page.models import User
from project.settings import DATABASE

log = None 

def render_login():
    global log

    if flask.request.method == 'POST':
        for user in User.query.filter_by(login = flask.request.form["name_or_email"]):
            if user.password == flask.request.form["password"] and user.login == flask.request.form["name_or_email"]:
                log = flask.request.form["name_or_email"]
                flask.session['log'] = log
                print(log)
                flask_login.login_user(user)
                return flask.redirect("/main2/")

            else:
                return flask.redirect("/login2")

    return flask.render_template(template_name_or_list= "login.html")