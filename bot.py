# Simple Telegram Premium Access Bot
# Install:
# pip install pyTelegramBotAPI

import telebot

TOKEN = "8599821431:AAHWT4Qr57pRZk_5w3lZrkm3Tyvp2Ga8uMo"
ADMIN = "@Yhunalm"

bot = telebot.TeleBot(TOKEN)

WELCOME = f"""
🔥 PREMIUM VIDEO ACCESS 🔥

💎 Price: ₹99 Only

✅ Pay using QR Code
📸 Send payment screenshot after payment

⏳ Access will be given after verification.

📩 Admin: {ADMIN}
"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, WELCOME)

@bot.message_handler(content_types=['photo'])
def payment_screenshot(message):
    bot.reply_to(
        message,
        "✅ Screenshot received.\nAdmin will verify payment soon."
    )

    # Forward screenshot to admin
    # Replace ADMIN_CHAT_ID with your Telegram numeric ID
    ADMIN_CHAT_ID = 
7831401352
    bot.forward_message(
        ADMIN_CHAT_ID,
        message.chat.id,
        message.message_id
    )

print("Bot Running...")
bot.infinity_polling()