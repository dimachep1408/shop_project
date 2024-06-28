import flask  # Імпорт фреймворку Flask / Importing the Flask framework
import flask_migrate  # Імпорт Flask-Migrate для міграцій бази даних / Importing Flask-Migrate for database migrations
import flask_sqlalchemy  # Імпорт Flask-SQLAlchemy для управління базою даних / Importing Flask-SQLAlchemy for database management
import os  # Імпорт модуля os для роботи з операційною системою / Importing os module for operating system functionality

shop = flask.Flask(
    import_name="settings",  # Встановлення імені для імпорту Flask додатка / Setting import name for the Flask app
    template_folder="project/templates",  # Встановлення шляху до теки з шаблонами / Setting template folder path
    instance_path=os.path.abspath(__file__ + "/.."),  # Встановлення шляху до інстанції для конфігурації / Setting instance path for configuration
    static_folder="/project/static/css"  # Встановлення шляху до теки зі статичними файлами / Setting static folder path
)

shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"  # Налаштування URI бази даних SQLite / Configuring SQLite database URI

DATABASE = flask_sqlalchemy.SQLAlchemy(app=shop)  # Створення екземпляру SQLAlchemy для додатка Flask / Creating SQLAlchemy database instance for the Flask app
MIGRATE = flask_migrate.Migrate(app=shop, db=DATABASE)  # Створення екземпляру Flask-Migrate для міграцій бази даних / Creating Flask-Migrate instance for database migrations
