from bale import MenuKeyboardMarkup, MenuKeyboardButton


def main_menu_keyboard():

    keyboard = MenuKeyboardMarkup()

    keyboard.add(
        MenuKeyboardButton("📅 ثبت نوبت"),
        row=1
    )
    keyboard.add(
        MenuKeyboardButton("📞 درخواست مشاوره"),
        row=1
    )

    keyboard.add(
        MenuKeyboardButton("💉 مراقبت‌های بعد از خدمات"),
        row=2
    )
    keyboard.add(
        MenuKeyboardButton("⏰ ثبت یادآوری زمان ترمیم"),
        row=2
    )

    keyboard.add(
        MenuKeyboardButton("🎉 جشنواره‌ها"),
        row=3
    )
    keyboard.add(
        MenuKeyboardButton("❓ سوالات متداول"),
        row=3
    )

    keyboard.add(
        MenuKeyboardButton("ℹ️ معرفی خدمات کلینیک"),
        row=4
    )

    return keyboard