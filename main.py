import telebot
from telebot import types

# Прямое указание токена, чтобы Render не тупил
API_TOKEN = '8202786671:AAEM6GVrNw_RTUGKO2_Q8rQ1ZLAoIjpxZqw'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # Твоя партнерская ссылка
    button = types.InlineKeyboardButton(
        text="🌐 ПЕРЕЙТИ К РЕГИСТРАЦИИ", 
        url="https://1wosdy.life/casino/list?open=register&p=8v9p"
    )
    markup.add(button)
    
    welcome_text = (
        "<b>ДОБРО ПОЖАЛОВАТЬ В ОФИЦИАЛЬНЫЙ ШЛЮЗ АВТОРИЗАЦИИ 1WIN</b>\n\n"
        "Ваш аккаунт подтвержден как приоритетный. Чтобы получить доступ к расширенным бонусам и моментальному выводу средств, выполните следующие действия:\n\n"
        "1. Нажмите кнопку ниже для перехода на официальное зеркало.\n"
        "2. Используйте промокод: <b>Hesoyam88</b> при регистрации.\n"
        "3. Пополните баланс и заберите бонус +500% к депозиту.\n\n"
        "<i>Данный шлюз работает в автоматическом режиме 24/7.</i>"
    )
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='html', reply_markup=markup)

if __name__ == '__main__':
    print("Бот запущен и готов к работе...")
    bot.infinity_polling()
