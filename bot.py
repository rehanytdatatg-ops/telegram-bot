import telebot

TOKEN = "8599821431:AAHWT4Qr57pRZk_5w3lZrkm3Tyvp2Ga8uMo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    photo = open("qr.jpg", "rb")

    bot.send_photo(
        message.chat.id,
        photo,
        caption="""
🔥 PREMIUM VIDEO ACCESS 🔥

💎 Price: ₹99 Only

✅ Scan QR & Pay
📸 Send payment screenshot

📩 Admin: @Yhunalm
"""
    )

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(
        message,
        "✅ Screenshot received.\nAdmin will verify payment."
    )

print("Bot Running...")
bot.infinity_polling()