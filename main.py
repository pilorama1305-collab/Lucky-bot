import telebot
from telebot import types

# Твой рабочий токен
API_TOKEN = '8202786671:AAEM6GVrNw_RTUGKO2_Q8rQ1ZLAoIjpxZqw'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # ТВОЯ НОВАЯ ССЫЛКА ЗДЕСЬ
    button = types.InlineKeyboardButton(
        text="🌐 ПЕРЕЙТИ К РЕГИСТРАЦИИ", 
        url="https://r1wgoph.life/casino/list?open=register&p=jwsf"
    )
    markup.add(button)
    
    welcome_text = (
        "<b>ДОБРО ПОЖА
    
