import telebot
from telebot import types
import os

# Берем токен из настроек Render (Environment Variables)
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# ТВОИ ДАННЫЕ (АКТУАЛЬНЫЕ)
PROMO = "Hesoyam88"
LINK = "https://r1wgoph.life/casino/list?open=register&p=jwsf" 

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "дружище"
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 ПЕРЕЙТИ К ИГРЕ", url=LINK)
    markup.add(btn)
    
    welcome_text = (
        f"🛡️ <b>1win | Официальный шлюз авторизации</b>\n\n"
        f"Здорово, {user_name}! Твой аккаунт успешно верифицирован для получения повышенного приветственного бонуса.\n\n"
        f"Чтобы закрепить за собой бонусный баланс:\n"
        f"1️⃣ Нажми кнопку <b>«ПЕРЕЙТИ К ИГРЕ»</b> ниже.\n"
        f"2️⃣ При регистрации введи секретный промокод: <code>{PROMO}</code>\n\n"
        f"🎁 <b>Твои бонусы сегодня:</b>\n"
        f"• <b>+500%</b> к первому депозиту\n"
        f"• <b>70 фриспинов</b> в топовых слотах\n"
        f"• Кэшбэк до <b>30%</b> каждую неделю\n\n"
        f"<i>⚠️ Внимание: Без ввода промокода бонусная программа не активируется.</i>"
    )
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='HTML', reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
    
