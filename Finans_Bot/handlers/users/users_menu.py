from aiogram import types
from loader import dp, bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from keyboards.user_keyboard import ReplyKeyboard, InlineKeyboard
from utils.misc.exchange_rates import USD_Value, EUR_Value, GBP_Value
from utils.misc.exchange_rates import СNY_Value, AED_Value, TRY_Value


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    name = message.from_user.first_name
    sticker_id = 'CAACAgIAAxkBAAEGH8xjTbfjLUTk0mpF7CEEEWRBRXFx0wAC9gUAAglLHRc7W0-qErCW_SoE'

    await bot.send_sticker(message.from_user.id, sticker=sticker_id)
    await message.answer(f'Здравствуйте, {name}, я бот, который поможет вам развиваться в области финансовой грамотности.', parse_mode='HTML', reply_markup=ReplyKeyboard)


@dp.message_handler(Text("Курс валют"))
async def rate(message: Message):
    await message.reply("Выберите валюту!", reply_markup=InlineKeyboard)

    @dp.callback_query_handler(text=["USD", "EUR", "GBP", "CNY", "AED", "TRY"])
    async def values(call: types.CallbackQuery):
        if call.data == "USD":
            value = USD_Value()
            await call.message.answer(f"На данный момент официальный курс Доллара составляет:  {value}  рублей")
        elif call.data == "EUR":
            value = EUR_Value()
            await call.message.answer(f"На данный момент официальный курс Евро составляет:  {value}  рублей")
        elif call.data == "GBP":
            value = GBP_Value()
            await call.message.answer(f"На данный момент официальный курс Фунта составляет:  {value}  рублей")
        elif call.data == "CNY":
            value = СNY_Value()
            await call.message.answer(f"На данный момент официальный курс Юаня составляет:  {value}  рублей")
        elif call.data == "AED":
            value = AED_Value()
            await call.message.answer(f"На данный момент официальный курс Дирхама составляет:  {value}  рублей")
        else:
            value = TRY_Value()
            await call.message.answer(f"На данный момент официальный курс Лиры составляет:  {value}  рублей")


@dp.message_handler(Text("Основные понятия"))
async def transactions_with_currencies(message: Message):
    with open('data_base//texts//basic_concepts.txt', 'r', encoding='utf-8') as text:
        dialog = text.read()

    await message.answer(text=dialog)


@dp.message_handler(Text("Полезные советы"))
async def useful_hints(message: Message):
    with open('data_base//texts//helpful_hints.txt', 'r', encoding='utf-8') as text:
        dialog = text.read()

    photo = open("data_base//images//finance.jpg", 'rb')

    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(text=dialog)


@dp.message_handler(Text("Куда инвестировать?"))
async def where_invests(message: Message):
    with open('data_base//texts//where_invest.txt', 'r', encoding='utf-8') as text:
        dialog = text.read()

    photo = open("data_base//images//investments.jpg", 'rb')

    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(text=dialog)


@dp.message_handler(Text("Где развиваться дальше?"))
async def where_invests(message: Message):
    with open('data_base//texts//whats_next.txt', 'r', encoding='utf-8') as text:
        dialog = text.read()

    sticker_id = "CAACAgIAAxkBAAEGPodjXU6B-H6zqINe8N_UTe55ODYrogACFQcAAglLHRfBIo4zI_q6lCoE"

    await bot.send_sticker(message.from_user.id, sticker=sticker_id)
    await message.answer(text=dialog)


