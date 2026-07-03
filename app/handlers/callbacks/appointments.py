from bale import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

from app.api.slots import get_slots


async def handle_appointment_callback(callback: CallbackQuery):
    
    if callback.data.startswith("appointment:"):
            

        service_id = int(callback.data.split(":")[1])

        slots = await get_slots()

        if not slots:
            await callback.message.reply("زمان خالی وجود ندارد")
            return


        keyboard = InlineKeyboardMarkup()

        row = 1

        for i,slot in enumerate(slots):
            keyboard.add(
                InlineKeyboardButton(
                    text=slot["start_time"],
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
        service_id = int(parts[1])
        slot_id = int(parts[2])

        # گرفتن user از backend
        from app.api.client import get_or_create_user

        user = await get_or_create_user(
            callback.message.chat.id,
            callback.message.chat.first_name,
            callback.message.chat.last_name or ""
        )

        # ثبت نوبت
        from app.api.appointments import create_appointment_api

        result = await create_appointment_api(
            user_id=user["id"],
            slot_id=slot_id,
            service_id=service_id
        )

        if not result:
            await callback.message.reply("خطا در ثبت نوبت")
            return

        await callback.message.reply(
            "✅ نوبت شما با موفقیت ثبت شد"
        )

        return