import telebot
from telebot import types
import os

# Твой токен
API_TOKEN = '8202786671:AAHEBj7ulltTuiiAC7Y27PFBiy6QRKgPBLg'
bot = telebot.TeleBot(API_TOKEN)

# Твоя ссылка
PARTNER_LINK = 'https://r1wgoph.life/casino/list?open=register'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="🚀 АКТИВИРОВАТЬ БОНУС X5 🚀", url=PARTNER_LINK)
    markup.add(btn)
    
    user_name = message.from_user.first_name if message.from_user.first_name else "дружище"
    
    welcome_text = (
        f"<b>Здорово, {user_name}! Лови момент!</b> 🍀\n\n"
        "Ты попал на закрытую раздачу бонусных инвайтов.\n"
        "Твой статус: <b>Подтвержден</b> ✅\n\n"
        "Твой первый депозит будет <b>умножен на 5 (X5)</b> автоматически.\n\n"
        "<b>Инструкция по активации:</b>\n"
        "1. Жми кнопку ниже.\n"
        "2. Пройди быструю регистрацию.\n"
        "3. Пополни баланс — бонус упадет моментально.\n\n"
        "<i>*Акция действует 24 часа. Успевай забрать куш!</i> 🎰"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='HTML')

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
  
