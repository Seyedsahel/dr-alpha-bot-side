from bale import InlineKeyboardMarkup, InlineKeyboardButton


def aftercares_keyboard(aftercares):

    keyboard = InlineKeyboardMarkup()

    row = 1

    for i, item in enumerate(aftercares):

        keyboard.add(
            InlineKeyboardButton(
                text=item["service_name"],
                callback_data=f"aftercare:{item['service_id']}"
            ),
            row=row
        )

        if (i + 1) % 2 == 0:
            row += 1

    return keyboard