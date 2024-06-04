import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from admin_app.models import Product
from project.settings import DATABASE
from project.settings import shop

def render_redact():
    global product

    if len(list(Product.query.all())) == 0:

        excel_path = os.path.abspath(__file__ + '/../static/Product.xlsx')
        data_excel = pandas.read_excel(io = excel_path, header = None, names = ["name", "price", "image", "count", "final_price"])
        for row in data_excel.iterrows():
            row_data = row[1]
            product = Product(
                name = row_data['name'],
                price = row_data['price'],
                image = row_data['image'],
                count = row_data['count'],
                final_price = row_data["final_price"]
            )
            DATABASE.session.add(product)
        DATABASE.session.commit()

    print(Product.query.all())

    name = flask.session.get('log')


    # Получаем абсолютный путь к папке images внутри admin_page/static
    uploads_dir2 = os.path.abspath(os.path.join(shop.root_path, "shop_page", "static", "images"))

    # Создаем директорию, если она не существует
    os.makedirs(uploads_dir2, exist_ok=True)

    # Собираем абсолютный путь к файлу



    if flask.request.method == "POST":

        try:
            try:

                file1 = flask.request.files["fileInput1"]
                file1.save(os.path.join(uploads_dir2, "1.png"))
            except:
                try:
                    file2 = flask.request.files["fileInput2"]
                    file2.save(os.path.join(uploads_dir2, "2.png"))
                except:

                    file3 = flask.request.files["fileInput3"]
                    file3.save(os.path.join(uploads_dir2, "3.png"))
        except:


            text = flask.request.form["InputModal"]

            print(text)


            flag = flask.session.get('flag')



            if flag == "rewrite4":
                product2 = Product.query.get_or_404(1)
                product2.name = text
                DATABASE.session.commit()


            if flag == "rewrite5":
                product2 = Product.query.get_or_404(2)
                product2.name = text
                DATABASE.session.commit()


            if flag == "rewrite6":
                product2 = Product.query.get_or_404(3)
                product2.name = text
                DATABASE.session.commit()


            
            if flag == "rewrite7":
                product2 = Product.query.get_or_404(1)
                product2.price = text
                product2.final_price = int(text) * 0.19
                DATABASE.session.commit()    

            if flag == "rewrite18":
                product2 = Product.query.get_or_404(2)
                product2.price = text
                product2.final_price = int(text) * 0.19
                DATABASE.session.commit()   

            if flag == "rewrite21":
                product2 = Product.query.get_or_404(3)
                product2.price = text
                product2.final_price = int(text) * 0.19
                DATABASE.session.commit()   


        # Сохраняем файл


        return flask.redirect("/admin/")



        print(DATABASE.session)

    return flask.render_template(template_name_or_list= "redact.html", log = name, products = Product.query.all(), flag = flask.session.get('flag'))