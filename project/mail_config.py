from flask_mail import Mail  # Імпорт класу Mail з Flask-Mail для роботи з електронною поштою / Importing the Mail class from Flask-Mail for email functionality
from .settings import shop  # Імпорт налаштувань магазину з модуля settings / Importing shop settings from the settings module

ADMINISTRATOR_ADDRESS = "chepikovdima1@gmail.com"  # Встановлення адреси адміністратора для електронної пошти / Setting administrator email address
ADMINISTRATOR_PASSWORD = "23456180D!m@"  # Встановлення пароля адміністратора для електронної пошти / Setting administrator email password

shop.config["MAIL_SERVER"] = "smtp.gmail.com"  # Налаштування SMTP сервера для Gmail / Configuring SMTP server for Gmail
shop.config["MAIL_PORT"] = 587  # Встановлення порту SMTP для Gmail / Setting SMTP port for Gmail
shop.config["MAIL_USE_TLS"] = True  # Включення використання TLS для шифрування електронної пошти / Enabling TLS encryption for secure email transmission
shop.config["MAIL_USERNAME"] = ADMINISTRATOR_ADDRESS  # Встановлення користувача електронної пошти (адреса адміністратора) / Setting email username (administrator's address)
shop.config["MAIL_PASSWORD"] = ADMINISTRATOR_PASSWORD  # Встановлення пароля електронної пошти (пароль адміністратора) / Setting email password (administrator's password)

mail = Mail(shop)  # Створення екземпляру Mail з налаштованим додатком Flask (shop) / Creating a Mail instance with the configured Flask application (shop)
