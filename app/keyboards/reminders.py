from bale import InlineKeyboardMarkup, InlineKeyboardButton


def reminder_services_keyboard(services):

    keyboard = InlineKeyboardMarkup()

    row = 1

    for i, service in enumerate(services):

        keyboard.add(
            InlineKeyboardButton(
                text=service["name"],
                callback_data=f"reminder_service:{service['id']}"
            ),
            row=row
        )

        if (i + 1) % 2 == 0:
            row += 1

    return keyboard