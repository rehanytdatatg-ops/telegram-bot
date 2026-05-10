import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ==========================================
# BOT SETTINGS
# ==========================================

TOKEN = "8796684139:AAErNtwcP5jbdAvSKXqjx7LQLM4aKQGyuKY"

ADMIN_ID = 7831401352
ADMIN_USERNAME = "@Yhunalm"

UPI_ID = "himanshudubey@fam"

# VIP LINKS
LITE_LINK = "https://t.me/+jinnhsyeEftlYTU0"
MEDIUM_LINK = "https://t.me/+jinnhsyeEftlYTU0"
PREMIUM_LINK = "https://t.me/+jinnhsyeEftlYTU0"

# ==========================================
# START BOT
# ==========================================

bot = telebot.TeleBot(TOKEN)

# Store selected plans
user_plan = {}

# ==========================================
# START COMMAND
# ==========================================

@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup(row_width=1)

    lite_btn = InlineKeyboardButton(
        "🥈 LITE VIP — ₹99",
        callback_data="lite"
    )

    medium_btn = InlineKeyboardButton(
        "🥇 MEDIUM VIP — ₹149",
        callback_data="medium"
    )

    premium_btn = InlineKeyboardButton(
        "👑 PREMIUM VIP — ₹199",
        callback_data="premium"
    )

    feature_btn = InlineKeyboardButton(
        "🔥 VIP FEATURES",
        callback_data="features"
    )

    review_btn = InlineKeyboardButton(
        "⭐ USER REVIEWS",
        callback_data="reviews"
    )

    admin_btn = InlineKeyboardButton(
        "📩 CONTACT ADMIN",
        url="https://t.me/Yhunalm"
    )

    markup.add(
        lite_btn,
        medium_btn,
        premium_btn,
        feature_btn,
        review_btn,
        admin_btn
    )

    photo = open("start.jpg", "rb")

    bot.send_photo(
        message.chat.id,
        photo,
        caption=f"""
✨👑 VERIFIED VIP ACCESS 👑✨

━━━━━━━━━━━━━━━

💎 Premium Telegram Experience
⚡ Fast Verification
🎬 HD Premium Content
🛡 Trusted Service
🚀 Instant Support

━━━━━━━━━━━━━━━

👑 VERIFIED ADMIN
{ADMIN_USERNAME}

👇 SELECT VIP PLAN BELOW
""",
        reply_markup=markup
    )

# ==========================================
# BUTTON HANDLER
# ==========================================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # ======================================
    # LITE VIP
    # ======================================

    if call.data == "lite":

        user_plan[call.message.chat.id] = "LITE VIP — ₹99"

        send_payment(call, "LITE VIP", "₹99")

    # ======================================
    # MEDIUM VIP
    # ======================================

    elif call.data == "medium":

        user_plan[call.message.chat.id] = "MEDIUM VIP — ₹149"

        send_payment(call, "MEDIUM VIP", "₹149")

    # ======================================
    # PREMIUM VIP
    # ======================================

    elif call.data == "premium":

        user_plan[call.message.chat.id] = "PREMIUM VIP — ₹199"

        send_payment(call, "PREMIUM VIP", "₹199")

    # ======================================
    # FEATURES
    # ======================================

    elif call.data == "features":

        bot.send_message(
            call.message.chat.id,
            """
✨🔥 VIP FEATURES 🔥✨

━━━━━━━━━━━━━━━

🥈 LITE VIP
✅ Basic Premium Access
✅ HD Content
✅ Fast Delivery

━━━━━━━━━━━━━━━

🥇 MEDIUM VIP
✅ Extra Premium Content
✅ Priority Support
✅ Better Experience

━━━━━━━━━━━━━━━

👑 PREMIUM VIP
✅ Full Premium Access
✅ Instant Priority Delivery
✅ Exclusive VIP Content
✅ Ultimate Experience
"""
        )

    # ======================================
    # REVIEWS
    # ======================================

    elif call.data == "reviews":

        bot.send_message(
            call.message.chat.id,
            """
⭐ USER REVIEWS ⭐

━━━━━━━━━━━━━━━

✅ Trusted Service
✅ Fast Verification
✅ Smooth Delivery
✅ Premium Experience

👑 VIP USERS LOVE IT
"""
        )

    # ======================================
    # PAYMENT DONE
    # ======================================

    elif call.data == "done":

        bot.send_message(
            call.message.chat.id,
            """
📸 SEND PAYMENT SCREENSHOT

⏳ WAITING FOR VERIFICATION...
"""
        )

# ==========================================
# PAYMENT FUNCTION
# ==========================================

def send_payment(call, plan_name, amount):

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
✨💸 {plan_name} PAYMENT 💸✨

━━━━━━━━━━━━━━━

💰 Amount: {amount}

🏦 UPI ID:
{UPI_ID}

✅ Pay Via QR or UPI
📸 Send Screenshot After Payment

⚡ Verification Usually Takes Few Minutes

━━━━━━━━━━━━━━━

👑 ADMIN:
{ADMIN_USERNAME}
""",
        reply_markup=markup
    )

# ==========================================
# SCREENSHOT HANDLER
# ==========================================

@bot.message_handler(content_types=['photo'])
def payment_screenshot(message):

    plan = user_plan.get(
        message.chat.id,
        "Unknown Plan"
    )

    # Reply to user
    bot.reply_to(
        message,
        f"""
✅ SCREENSHOT RECEIVED

📦 Selected Plan:
{plan}

⏳ WAITING FOR ADMIN VERIFICATION...
"""
    )

    # Forward screenshot to admin
    bot.forward_message(
        ADMIN_ID,
        message.chat.id,
        message.message_id
    )

    # Admin approve/reject buttons
    markup = InlineKeyboardMarkup(row_width=2)

    approve_btn = InlineKeyboardButton(
        "✅ APPROVE",
        callback_data=f"approve_{message.chat.id}"
    )

    reject_btn = InlineKeyboardButton(
        "❌ REJECT",
        callback_data=f"reject_{message.chat.id}"
    )

    markup.add(
        approve_btn,
        reject_btn
    )

    # Notify admin
    bot.send_message(
        ADMIN_ID,
        f"""
📩 NEW PAYMENT SCREENSHOT

👤 User:
{message.from_user.first_name}

🆔 User ID:
{message.chat.id}

📦 Plan:
{plan}
""",
        reply_markup=markup
    )

# ==========================================
# ADMIN ACTIONS
# ==========================================

@bot.callback_query_handler(
    func=lambda call:
    call.data.startswith("approve_") or
    call.data.startswith("reject_")
)
def admin_action(call):

    # ======================================
    # APPROVE USER
    # ======================================

    if call.data.startswith("approve_"):

        user_id = int(
            call.data.split("_")[1]
        )

        plan = user_plan.get(
            user_id,
            "LITE VIP — ₹99"
        )

        # Select VIP link
        if "LITE" in plan:
            vip_link = LITE_LINK

        elif "MEDIUM" in plan:
            vip_link = MEDIUM_LINK

        else:
            vip_link = PREMIUM_LINK

        bot.send_message(
            user_id,
            f"""
✨✅ PAYMENT VERIFIED ✅✨

🎉 VIP ACCESS APPROVED

📦 PLAN:
{plan}

🔗 VIP LINK:
{vip_link}

⚠ DO NOT SHARE THIS LINK
"""
        )

        bot.answer_callback_query(
            call.id,
            "USER APPROVED"
        )

    # ======================================
    # REJECT USER
    # ======================================

    elif call.data.startswith("reject_"):

        user_id = int(
            call.data.split("_")[1]
        )

        bot.send_message(
            user_id,
            """
❌ PAYMENT NOT VERIFIED

📩 PLEASE CONTACT ADMIN
"""
        )

        bot.answer_callback_query(
            call.id,
            "USER REJECTED"
        )

# ==========================================
# RUN BOT
# ==========================================

print("🚀 VIP PREMIUM BOT RUNNING...")

bot.infinity_polling()