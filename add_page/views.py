import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from admin_app.models import Product
from project.settings import DATABASE
from project.settings import shop

def render_add():
    global product





    if flask.request.method == "POST":

        try:

            product = Product(
                name = flask.request.form["Name"],
                price = flask.request.form["Price"],
                image = str(int(str(Product.query.all()[-1]).split(",")[0].split("id - ")[1]) + 1) + ".png",
                final_price = int(flask.request.form["Price"]) - int(flask.request.form["Price"]) * 0.19
            )

        except:

            product = Product(
                name = flask.request.form["Name"],
                price = flask.request.form["Price"],
                image = "1.png",
                final_price = int(flask.request.form["Price"]) - int(flask.request.form["Price"]) * 0.19
            )
            
        DATABASE.session.add(product)
        DATABASE.session.commit()





        uploads_dir2 = os.path.abspath(os.path.join(shop.root_path, "shop_page", "static", "images"))

        # Создаем директорию, если она не существует
        os.makedirs(uploads_dir2, exist_ok=True)

        file1 = flask.request.files["Image"]
        file1.save(os.path.join(uploads_dir2, product.image ))




        return flask.redirect("/admin/")


    return flask.render_template(template_name_or_list= "add.html", products = Product.query.all(), flag = flask.session.get('flag'))