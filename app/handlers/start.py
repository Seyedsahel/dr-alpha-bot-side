from bale import Message

from app.bot import bot


@bot.event
async def on_ready():
    print(f"{bot.user.username} is Ready!")


@bot.event
async def on_message(message: Message):

    if message.content != "/start":
        return

    await message.reply(
        "سلام 🌸\n"
        "به ربات کلینیک دکتر کامرانی خوش آمدید."
    )