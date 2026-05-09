import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================
# BOT SETTINGS
# =========================

TOKEN = "8796684139:AAErNtwcP5jbdAvSKXqjx7LQLM4aKQGyuKY"

ADMIN_ID = 7831401352
ADMIN_USERNAME = "@Yhunalm"

UPI_ID = "himanshudubey@fam"

VIP_LINK = "https://t.me/+jinnhsyeEftlYTU0"

# =========================
# START BOT
# =========================

bot = telebot.TeleBot(TOKEN)

# Store pending users
pending_users = {}

# =========================
# START COMMAND
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup(row_width=1)

    buy_btn = InlineKeyboardButton(
        "💎 BUY PREMIUM ₹99",
        callback_data="buy"
    )

    feature_btn = InlineKeyboardButton(
        "🔥 VIP FEATURES",
        callback_data="features"
    )

    admin_btn = InlineKeyboardButton(
        "📩 CONTACT ADMIN",
        url="https://t.me/Yhunalm"
    )

    markup.add(
        buy_btn,
        feature_btn,
        admin_btn
    )

    photo = open("start.jpg", "rb")

    bot.send_photo(
        message.chat.id,
        photo,
        caption=f"""
🔥 VERIFIED PREMIUM ACCESS 🔥

━━━━━━━━━━━━━━━

✅ Premium VIP Content
✅ Trusted Service
✅ Fast Verification
✅ HD Quality Access

💎 Premium Plan: ₹99

━━━━━━━━━━━━━━━

🛡 Verified Admin:
{ADMIN_USERNAME}

👇 Choose Option Below
""",
        reply_markup=markup
    )

# =========================
# BUTTON HANDLER
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # BUY BUTTON
    if call.data == "buy":

        qr = open("qr.jpg", "rb")

        markup = InlineKeyboardMarkup(row_width=1)

        done_btn = InlineKeyboardButton(
            "✅ PAYMENT DONE",
            callback_data="done"
        )

        markup.add(done_btn)

        bot.send_photo(
            call.message.chat.id,
            qr,
            caption=f"""
💸 PREMIUM PAYMENT

━━━━━━━━━━━━━━━

💎 Amount: ₹99

✅ Pay via UPI or QR

🏦 UPI ID:
`{UPI_ID}`

📸 Send payment screenshot after payment.

⏳ Verification usually takes few minutes.

━━━━━━━━━━━━━━━

🛡 Admin:
{ADMIN_USERNAME}
""",
            parse_mode="Markdown",
            reply_markup=markup
        )

    # FEATURES BUTTON
    elif call.data == "features":

        bot.send_message(
            call.message.chat.id,
            """
🔥 VIP FEATURES

━━━━━━━━━━━━━━━

✅ HD Premium Content
✅ VIP Private Access
✅ Fast Support
✅ Secure Access
✅ Better Experience

💎 Premium Price: ₹99
"""
        )

    # PAYMENT DONE BUTTON
    elif call.data == "done":

        bot.send_message(
            call.message.chat.id,
            """
📸 Please send payment screenshot.

⏳ Waiting for verification.
"""
        )

# =========================
# SCREENSHOT HANDLER
# =========================

@bot.message_handler(content_types=['photo'])
def payment_screenshot(message):

    pending_users[message.chat.id] = True

    bot.reply_to(
        message,
        """
✅ PAYMENT SCREENSHOT RECEIVED

⏳ Admin will verify shortly.
"""
    )

    # Forward screenshot to admin
    bot.forward_message(
        ADMIN_ID,
        message.chat.id,
        message.message_id
    )

    # Admin buttons
    markup = InlineKeyboardMarkup()

    approve_btn = InlineKeyboardButton(
        "✅ APPROVE",
        callback_data=f"approve_{message.chat.id}"
    )

    reject_btn = InlineKeyboardButton(
        "❌ REJECT",
        callback_data=f"reject_{message.chat.id}"
    )

    markup.add(approve_btn, reject_btn)

    bot.send_message(
        ADMIN_ID,
        f"""
📩 New payment screenshot received.

👤 User ID:
{message.chat.id}
""",
        reply_markup=markup
    )

# =========================
# ADMIN APPROVAL SYSTEM
# =========================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("approve_") or
    call.data.startswith("reject_")
)
def admin_actions(call):

    # APPROVE
    if call.data.startswith("approve_"):

        user_id = int(call.data.split("_")[1])

        bot.send_message(
            user_id,
            f"""
✅ PAYMENT VERIFIED

🎉 VIP ACCESS APPROVED

🔗 VIP LINK:
{VIP_LINK}

⚠ Do not share link.
"""
        )

        bot.answer_callback_query(
            call.id,
            "User Approved"
        )

    # REJECT
    elif call.data.startswith("reject_"):

        user_id = int(call.data.split("_")[1])

        bot.send_message(
            user_id,
            """
❌ PAYMENT NOT VERIFIED

Please contact admin.
"""
        )

        bot.answer_callback_query(
            call.id,
            "User Rejected"
        )

# =========================
# RUN BOT
# =========================

print("🚀 Premium VIP Bot Running...")
bot.infinity_polling()