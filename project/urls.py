import main_page  # Імпорт головної сторінки / Importing the main page
import registration_page  # Імпорт сторінки реєстрації / Importing the registration page
from .settings import shop  # Імпорт налаштувань магазину / Importing shop settings
import login_page  # Імпорт сторінки входу / Importing the login page
import login_page2  # Імпорт другої сторінки входу / Importing the second login page
import main_page2  # Імпорт другої головної сторінки / Importing the second main page
import registration_page2  # Імпорт другої сторінки реєстрації / Importing the second registration page
import shop_page  # Імпорт сторінки магазину / Importing the shop page
import basket_page  # Імпорт сторінки кошика / Importing the basket page
import admin_app  # Імпорт адміністративної сторінки / Importing the admin page
import redact_page  # Імпорт сторінки редагування / Importing the redact page
import add_page  # Імпорт сторінки додавання / Importing the add page
import order_page  # Імпорт сторінки замовлення / Importing the order page

main_page.main.add_url_rule(rule="/", view_func=main_page.render_main)  # Додавання правила URL для головної сторінки / Adding URL rule for the main page
registration_page.registration.add_url_rule(rule="/registration/", view_func=registration_page.render_registration, methods=["GET", "POST"])  # Додавання правила URL для сторінки реєстрації / Adding URL rule for the registration page
login_page.login.add_url_rule(rule="/login/", view_func=login_page.render_login, methods=["GET", "POST"])  # Додавання правила URL для сторінки входу / Adding URL rule for the login page
login_page2.login2.add_url_rule(rule="/login2/", view_func=login_page2.render_login2, methods=["GET", "POST"])  # Додавання правила URL для другої сторінки входу / Adding URL rule for the second login page
main_page2.main2.add_url_rule(rule="/main2/", view_func=main_page2.render_main2, methods=["GET", "POST"])  # Додавання правила URL для другої головної сторінки / Adding URL rule for the second main page
registration_page2.registration2.add_url_rule(rule="/registration2/", view_func=registration_page2.render_registration2, methods=["GET", "POST"])  # Додавання правила URL для другої сторінки реєстрації / Adding URL rule for the second registration page
shop_page.shop.add_url_rule(rule="/shop/", view_func=shop_page.render_shop, methods=["GET", "POST"])  # Додавання правила URL для сторінки магазину / Adding URL rule for the shop page
basket_page.basket.add_url_rule(rule="/basket/", view_func=basket_page.render_basket, methods=["GET", "POST"])  # Додавання правила URL для сторінки кошика / Adding URL rule for the basket page
admin_app.admin.add_url_rule(rule="/admin/", view_func=admin_app.render_admin, methods=["GET", "POST"])  # Додавання правила URL для адміністративної сторінки / Adding URL rule for the admin page
redact_page.redact.add_url_rule(rule="/admin/redact/", view_func=redact_page.render_redact, methods=["GET", "POST"])  # Додавання правила URL для сторінки редагування / Adding URL rule for the redact page
add_page.add.add_url_rule(rule="/shop/add/", view_func=add_page.render_add, methods=["GET", "POST"])  # Додавання правила URL для сторінки додавання / Adding URL rule for the add page
order_page.order.add_url_rule(rule="/basket/order/", view_func=order_page.render_order, methods=["GET", "POST"])  # Додавання правила URL для сторінки замовлення / Adding URL rule for the order page

shop.register_blueprint(blueprint=main_page2.main2)  # Реєстрація блоку коду для другої головної сторінки / Registering blueprint for the second main page
shop.register_blueprint(blueprint=main_page.main)  # Реєстрація блоку коду для головної сторінки / Registering blueprint for the main page
shop.register_blueprint(blueprint=registration_page.registration)  # Реєстрація блоку коду для сторінки реєстрації / Registering blueprint for the registration page
shop.register_blueprint(blueprint=login_page.login)  # Реєстрація блоку коду для сторінки входу / Registering blueprint for the login page
shop.register_blueprint(blueprint=login_page2.login2)  # Реєстрація блоку коду для другої сторінки входу / Registering blueprint for the second login page
shop.register_blueprint(blueprint=registration_page2.registration2)  # Реєстрація блоку коду для другої сторінки реєстрації / Registering blueprint for the second registration page
shop.register_blueprint(blueprint=shop_page.shop)  # Реєстрація блоку коду для сторінки магазину / Registering blueprint for the shop page
shop.register_blueprint(blueprint=basket_page.basket)  # Реєстрація блоку коду для сторінки кошика / Registering blueprint for the basket page
shop.register_blueprint(blueprint=admin_app.admin)  # Реєстрація блоку коду для адміністративної сторінки / Registering blueprint for the admin page
shop.register_blueprint(blueprint=redact_page.redact)  # Реєстрація блоку коду для сторінки редагування / Registering blueprint for the redact page
shop.register_blueprint(blueprint=add_page.add)  # Реєстрація блоку коду для сторінки додавання / Registering blueprint for the add page
shop.register_blueprint(blueprint=order_page.order)  # Реєстрація блоку коду для сторінки замовлення / Registering blueprint for the order page
