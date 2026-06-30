from bale import Message, InputFile

from app.bot import bot
from app.api.festivals import get_festivals


@bot.event
async def festivals_handler(message: Message):

    if message.text != "🎉 جشنواره‌ها":
        return

    festivals = await get_festivals()

    if not festivals:
        await message.reply("متاسفانه در حال حاضر جشنواره فعالی وجود ندارد")
        return
    
    for festival in festivals:
        caption = (
            f"🎉 {festival['title']}\n\n"
            f"{festival['description']}"
        )
        # if festival["image_url"]:
        #     await message.reply_photo(
        #         InputFile(festival["image_url"]),
        #         caption=caption
        #     )
        # else:
        #     await message.reply(caption)
        await message.reply(caption)
