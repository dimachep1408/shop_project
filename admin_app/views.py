import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from .models import Product
from project.settings import DATABASE



def render_admin():
    global product, count

    



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


    

    if flask.request.method == "POST":
        btn = flask.request.form.get("rewrite")
        button_delete = flask.request.form.get("delete")

        if btn == None:
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
                
            write = product.query.get_or_404(flask.request.form.get("delete"))
            DATABASE.session.delete(write)
            DATABASE.session.commit()

            

            count = 1
            index = 1



            print(int(flask.request.form.get("delete")))
            for product in Product.query.all():            
                try:
                    product2 = Product.query.get(int(button_delete) + count) 
                    # print("aushdbfiuaehbui" , int(str(product).split(",")[0].split("id - ")[1]))
                    product2.id = count
                    print(product2.id)

                    print(count, index)
                except:
                    pass

                
                

                    
                count += 1


            DATABASE.session.commit()
            



            
            print(Product.query.all())




        else:
            flask.session['flag'] = btn
            




            print(btn)
            return flask.redirect("/admin/redact/")




    name = flask.session.get('log')

    # if flask.request.method == "POST":
    #     return flask.redirect("/admin/redact/")

    
    users = User.query.filter_by(is_admin = True).all()
    
    nicknames = []






    for user in users:
        nicknames.append(str(user).split(":")[1])
        

    for nickname in nicknames:
        print(nickname)
        print(name)

        if nickname == " " + name:
            return flask.render_template(template_name_or_list= "admin.html", log = name, products = Product.query.all())
    return flask.redirect("/shop/") 


