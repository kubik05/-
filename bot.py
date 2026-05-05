import telebot
import random
import json

TOKEN = "8677332922:AAG0gdvIcQKVrD-ljmfq0IF8-tG7M2bebGE"
bot = telebot.TeleBot(TOKEN)

users = {}
try:
    with open('users.json','r') as f:
        users = json.load(f)
except:
    users = {}

def save_users():
    with open('users.json','w') as f:
        json.dump(users,f)

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    if uid not in users:
        users[uid] = {'name':message.from_user.first_name,'money':100}
        save_users()
    bot.reply_to(message,f"⚔️ Я Ахилес, сын Пилея!\nДобро пожаловать, {message.from_user.first_name}!\n💰 {users[uid]['money']} монет\n/help — команды")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message,"""⚔️ КОМАНДЫ:
/start — Приветствие
/help — Команды
/money — Баланс
/coin — Монетка
/farm — Ферма
/duel — Дуэль
/echo — Повтор
/poem — Стих""")

@bot.message_handler(commands=['money'])
def money_cmd(message):
    uid = str(message.from_user.id)
    if uid not in users:
        users[uid] = {'name':message.from_user.first_name,'money':100}
        save_users()
    bot.reply_to(message,f"🪙 {users[uid]['money']} монет")

@bot.message_handler(commands=['coin'])
def coin_cmd(message):
    bot.reply_to(message,f"🪙 {random.choice(['Орёл','Решка'])}!")

@bot.message_handler(commands=['farm'])
def farm_cmd(message):
    uid = str(message.from_user.id)
    if uid not in users:
        users[uid] = {'name':message.from_user.first_name,'money':100}
    earned = random.randint(10,50)
    users[uid]['money'] += earned
    save_users()
    bot.reply_to(message,f"🌾 Урожай: {random.choice(['🥕 Морковь','🍅 Помидор','🎃 Тыква'])}!\n+{earned}🪙\nБаланс: {users[uid]['money']}")

@bot.message_handler(commands=['duel'])
def duel_cmd(message):
    uid = str(message.from_user.id)
    if uid not in users:
        users[uid] = {'name':message.from_user.first_name,'money':100}
    if users[uid]['money'] < 20:
        bot.reply_to(message,"Нет 20🪙!")
        return
    users[uid]['money'] -= 20
    if random.random() > 0.5:
        reward = random.randint(30,80)
        users[uid]['money'] += reward
        bot.reply_to(message,f"⚔️ Победа! +{reward}🪙")
    else:
        bot.reply_to(message,"💀 Поражение... -20🪙")
    save_users()

@bot.message_handler(commands=['echo'])
def echo_cmd(message):
    text = message.text.replace('/echo','').strip()
    if text:
        bot.reply_to(message,text)
    else:
        bot.reply_to(message,"Напиши текст: /echo привет")

@bot.message_handler(commands=['poem'])
def poem_cmd(message):
    poems = [
        "Гнев, богиня, воспой Ахиллеса, Пелеева сына...",
        "Лучше быть живым рабом, чем мёртвым царём.",
        "Я Ахилес, сын Пилея! Кто бросит мне вызов?"
    ]
    bot.reply_to(message,f"📜 {random.choice(poems)}")

print("⚔️ Ахилес готов!")
bot.infinity_polling()
