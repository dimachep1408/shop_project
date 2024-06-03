import flask
from .models import User
from project.settings import DATABASE

def render_registration():
    if flask.request.method == 'POST':
        user = User(login = flask.request.form['name'], 
                    password = flask.request.form["password"], 
                    email = flask.request.form["email"], 
                    password_confirm = flask.request.form["password_confirm"],
                    is_admin = False
                    )
        
        
        
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            return flask.redirect("/registration2")
        except:
            return 'ERROR'
    return flask.render_template(template_name_or_list= "registration.html")