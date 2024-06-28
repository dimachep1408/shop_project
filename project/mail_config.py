from flask_mail import Mail
from .settings import shop

ADMINISTRATOR_ADDRESS = "chepikovdima1@gmail.com"
ADMINISTRATOR_PASSWORD = "23456180D!m@"

shop.config["MAIL_SERVER"] = "smtp.gmail.com"
shop.config["MAIL_PORT"] = 587
shop.config["MAIL_USE_TLS"] = True
shop.config["MAIL_USERNAME"] = ADMINISTRATOR_ADDRESS
shop.config["MAIL_PASSWORD"] = ADMINISTRATOR_PASSWORD

mail = Mail(shop)