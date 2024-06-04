import main_page
import registration_page
from .settings import shop
import login_page
import login_page2
import main_page2
import registration_page2
import shop_page
import basket_page
import admin_app
import redact_page

main_page.main.add_url_rule(rule = "/", view_func= main_page.render_main)
registration_page.registration.add_url_rule(rule = "/registration/", view_func= registration_page.render_registration, methods = ["GET", "POST"])
login_page.login.add_url_rule(rule = "/login/", view_func= login_page.render_login, methods = ["GET", "POST"])
login_page2.login2.add_url_rule(rule = "/login2/",view_func = login_page2.render_login2, methods = ["GET", "POST"])
main_page2.main2.add_url_rule(rule = "/main2/", view_func = main_page2.render_main2, methods = ["GET", "POST"])
registration_page2.registration2.add_url_rule(rule= "/registration2/", view_func= registration_page2.render_registration2, methods = ["GET", "POST"])
shop_page.shop.add_url_rule(rule= "/shop/", view_func = shop_page.render_shop, methods = ["GET", "POST"])
basket_page.basket.add_url_rule(rule= "/basket/", view_func = basket_page.render_basket, methods = ["GET", "POST"])
admin_app.admin.add_url_rule(rule="/admin/", view_func= admin_app.render_admin, methods = ["GET", "POST"])
redact_page.redact.add_url_rule(rule = "/admin/redact/", view_func = redact_page.render_redact, methods = ["GET", "POST"])

shop.register_blueprint(blueprint = main_page2.main2)
shop.register_blueprint(blueprint = main_page.main)
shop.register_blueprint(blueprint = registration_page.registration)
shop.register_blueprint(blueprint = login_page.login)
shop.register_blueprint(blueprint = login_page2.login2)
shop.register_blueprint(blueprint = registration_page2.registration2)
shop.register_blueprint(blueprint = shop_page.shop)
shop.register_blueprint(blueprint = basket_page.basket)
shop.register_blueprint(blueprint = admin_app.admin)
shop.register_blueprint(blueprint= redact_page.redact)