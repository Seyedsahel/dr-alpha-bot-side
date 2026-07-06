from bale import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )
from app.api.slots import get_slots


async def handle_appointment_callback(callback: CallbackQuery):

    if callback.data.startswith("appointment:"):

        try:

         service_id = int(callback.data.split(":")[1])
        except (ValueError , IndexError):
            await callback.message.reply("⚠️ درخواست نا معتبر است")
            return
        
        slots = await get_slots()

        if not slots:
            await callback.message.reply("زمان خالی وجود ندارد")
            return

        keyboard = InlineKeyboardMarkup()
        row = 1

        for i, slot in enumerate(slots):
            keyboard.add(
                InlineKeyboardButton(
                    text=slot["start_time_jalali"],
                    callback_data=f"appointment_slot:{service_id}:{slot['id']}"
                ),
                row=row
            )
            if (i + 1) % 2 == 0:
                row += 1

        await callback.message.reply(
            "⏰ لطفاً زمان مورد نظر را انتخاب کنید:",
            components=keyboard
        )
        return True

    elif callback.data.startswith("appointment_slot:"):

        parts = callback.data.split(":")

        try:
            service_id = int(parts[1])
            slot_id = int(parts[2])
        except (ValueError, IndexError):
            await callback.message.reply("⚠️ درخواست نا معتبر است")
            return

        from app.api.client import get_or_create_user
        user = await get_or_create_user(
            callback.message.chat.id,
            callback.message.chat.first_name,
            callback.message.chat.last_name or ""
        )

        from app.api.appointments import create_appointment_api
        result, error = await create_appointment_api(
            user_id=user["id"],
            slot_id=slot_id,
            service_id=service_id
        )

        if error:
            await callback.message.reply(f"⚠️ {error}")
            return

        await callback.message.reply(
            "✅ نوبت شما با موفقیت ثبت شد"
        )
        return