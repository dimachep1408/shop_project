from project.settings import DATABASE
import flask_login

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    login = DATABASE.Column(DATABASE.String(50), nullable = False)
    email = DATABASE.Column(DATABASE.String(256), nullable = False)
    password = DATABASE.Column(DATABASE.String(50), nullable = False)
    password_confirm = DATABASE.Column(DATABASE.String(50), nullable = False)
    is_admin = DATABASE.Column(DATABASE.Boolean, default = False, nullable = False)
    def __repr__(self) -> str:
        return f"user : {self.login}"
    


