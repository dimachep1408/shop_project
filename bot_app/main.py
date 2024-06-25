import telebot
import sqlite3
import os

token = "7391868431:AAHDQsdCh6GH1Po-z9Bv4FNPgEtv_h2gIR4"
bot = telebot.TeleBot(token= token)

db = sqlite3.connect(os.path.abspath("/shop_project-2/project/data.db"), check_same_thread=False)
cursor = db.cursor()

def get_users():
    users = []
    cursor.execute("SELECT login, is_admin FROM user")
    for name, is_admin in cursor.fetchall():
        users.append(f"{name}-{is_admin}")
    return users

def get_products():
    products = []
    cursor.execute("SELECT name, id FROM product")
    for name, id in cursor.fetchall():
        products.append(f"{id}-{name}")

    return products

list_users = get_users()

button_show_users = telebot.types.InlineKeyboardButton(text="Get users", callback_data="button1")
button_show_products = telebot.types.InlineKeyboardButton(text= "Get products", callback_data= "button_show_products")
button_add_product = telebot.types.InlineKeyboardButton(text= "Add product", callback_data= "button_add_product")
keyboard1 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_show_users], [button_show_products], [button_add_product]])

button_add_admin = telebot.types.InlineKeyboardButton(text="Add admin", callback_data="button2")
button_demote_admin = telebot.types.InlineKeyboardButton(text="Demote admin", callback_data="button3")
keyboard2_1 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_add_admin]])
keyboard2_2 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_demote_admin]])


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="Hello!", reply_markup=keyboard1)


@bot.message_handler()
def start(message: telebot.types.Message):
    global id,name,price
    products = get_products()
    try:
        if products == []:
            id = 1
        else:
            id = int(products[-1].split("-")[0]) + 1
        name = message.text.split(",")[0]
        price = message.text.split(",")[1]
        discount = message.text.split(",")[2]

    except:
        pass
    cursor.execute(f"INSERT INTO product(name, price, image, final_price) VALUES('{name}', '{price}', '{str(id) + '.png'}', '{int(price) - int(price) * 0.19}')")
    db.commit()
    bot.send_message(chat_id= message.chat.id, text= "Now Send Image")

    

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def show_users(callback: telebot.types.CallbackQuery):
    global list_users
    list_users = get_users()
    for user in list_users:
        if user.split("-")[1] == "0":
            bot.send_message(chat_id=callback.message.chat.id, text=f"{user}", reply_markup=keyboard2_1)
        elif user.split("-")[1] == "1":
            bot.send_message(chat_id=callback.message.chat.id, text=f"{user}", reply_markup=keyboard2_2)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = os.path.abspath(__file__ + f"/../../shop_page/static/images/{str(id) + '.png'}")
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Image was save')



@bot.callback_query_handler(func=lambda call: call.data == "button_show_products")
def get_all_products(callback: telebot.types.CallbackQuery):
    list_products = get_products()
    for product_name in list_products:
        bot.send_message(chat_id=callback.message.chat.id, text=f"{product_name}")

@bot.callback_query_handler(func=lambda call: call.data == "button_add_product")
def add_products(callback: telebot.types.CallbackQuery):
    bot.send_message(chat_id=callback.message.chat.id, text="Send message like this:\n'name, price, discount' \n\nexample:\nlaptop, 49000, 50")
    name = ""
    price = "1000"
    final_price = int(price) - int(price) * 0.19


@bot.callback_query_handler(func=lambda call: call.data in ["button2", "button3"])
def modify_user(callback: telebot.types.CallbackQuery):
    name = callback.message.text.split("-")[0]
    cursor.execute("SELECT id, is_admin FROM user WHERE login = ?", (name))
    user = cursor.fetchone()
    if user:
        user_id, is_admin = user
        new_status = 1 if callback.data == "button2" else 0
        cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", (new_status, user_id))
        db.commit()
        status_text = "is admin now" if new_status == 1 else "is not admin now"
        bot.send_message(chat_id=callback.message.chat.id, text=f"{name} {status_text}")
    else:
        bot.send_message(chat_id=callback.message.chat.id, text="User not found")

bot.infinity_polling()
