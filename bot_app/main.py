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

list_users = get_users()

button_show_users = telebot.types.InlineKeyboardButton(text="Show users", callback_data="button1")
keyboard1 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_show_users]])

button_add_admin = telebot.types.InlineKeyboardButton(text="Add admin", callback_data="button2")
button_demote_admin = telebot.types.InlineKeyboardButton(text="Demote admin", callback_data="button3")
keyboard2_1 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_add_admin]])
keyboard2_2 = telebot.types.InlineKeyboardMarkup(keyboard=[[button_demote_admin]])


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="Hello!", reply_markup=keyboard1)


@bot.callback_query_handler(func=lambda call: call.data == "button1")
def show_users(callback: telebot.types.CallbackQuery):
    global list_users
    list_users = get_users()
    for user in list_users:
        if user.split("-")[1] == "0":
            bot.send_message(chat_id=callback.message.chat.id, text=f"{user}", reply_markup=keyboard2_1)
        elif user.split("-")[1] == "1":
            bot.send_message(chat_id=callback.message.chat.id, text=f"{user}", reply_markup=keyboard2_2)


@bot.callback_query_handler(func=lambda call: call.data in ["button2", "button3"])
def modify_user(callback: telebot.types.CallbackQuery):
    name = callback.message.text.split("-")[0]
    cursor.execute("SELECT id, is_admin FROM user WHERE login = ?", (name,))
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
