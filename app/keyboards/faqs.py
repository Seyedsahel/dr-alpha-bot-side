from bale import InlineKeyboardMarkup, InlineKeyboardButton


def faqs_keyboard(faqs):

    keyboard = InlineKeyboardMarkup()

    row = 1

    for faq in faqs:

        keyboard.add(
            InlineKeyboardButton(
                text=faq["question"],
                callback_data=f"faq:{faq['id']}"
            ),
            row=row
        )

        row += 1

    return keyboard