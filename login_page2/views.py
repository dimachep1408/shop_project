import flask
import flask_login
from registration_page.models import User
from project.settings import DATABASE

def render_login2(): 
    if flask.request.method == 'POST':
        for user in User.query.filter_by(login = flask.request.form["name_or_email"]):
            if user.password == flask.request.form["password"]:
                flask_login.login_user(user)
                return "Вы успешно авторизировались"
            else:
                return flask.redirect("/login2")
    return flask.render_template(template_name_or_list= "login2.html")