import flask
import flask_migrate
import flask_sqlalchemy
import os


shop = flask.Flask(
    import_name= "settings",
    template_folder= "project/templates",
    instance_path= os.path.abspath(__file__ + "/.."),
    static_folder= "/project/static/css"
)

shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = shop)
MIGRATE = flask_migrate.Migrate(app= shop, db = DATABASE)