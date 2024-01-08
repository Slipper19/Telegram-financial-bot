from aiogram import types
from loader import dp, bot


@dp.message_handler(commands=["about_me"])
async def start(message: types.Message):
    with open('data_base//texts//about_me.txt', 'r', encoding='utf-8') as text:
        dialog = text.read()

    sticker_id = "CAACAgIAAxkBAAEGQGNjXm9mFq8Z27NCBiCLJcv48k_KqAAC7QUAAglLHRcdcafiq2XVEioE"

    await bot.send_sticker(message.from_user.id, sticker=sticker_id)
    await message.answer(text=dialog, )
