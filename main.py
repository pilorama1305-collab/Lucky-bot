import telebot
from telebot import types
import os
import http.server
import socketserver
import threading

# Твой рабочий токен
API_TOKEN = '8202786671:AAEM6GVrNw_RTUGKO2_Q8rQ1ZLAoIjpxZqw'
bot = telebot.TeleBot(API_TOKEN)

# --- КОСТЫЛЬ ДЛЯ RENDER (ЧТОБЫ НЕ БЫЛО ОШИБКИ PORT SCAN) ---
def run_dummy_server():
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args): return # Чтобы не гадить в логи
    
    port = int(os.environ.get("PORT", 8080))
    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        print(f"Заглушка запущена на порту {port}")
        httpd.serve_forever()

# Запускаем заглушку в отдельном потоке
threading.Thread(target=run_dummy_server, daemon=True).start()
# ---------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
        text="🌐 ПЕРЕЙТИ К РЕГИСТРАЦИИ", 
        url="https://r1wgoph.life/casino/list?open=register&p=jwsf"
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
    try:
        print("Бот запущен и костыль активен...")
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        
