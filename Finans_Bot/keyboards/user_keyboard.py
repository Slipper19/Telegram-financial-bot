from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

ReplyKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Курс валют"),
            KeyboardButton(text="Основные понятия")
        ],
        [
            KeyboardButton(text="Полезные советы"),
            KeyboardButton(text="Куда инвестировать?")
        ],
        [
            KeyboardButton(text="Где развиваться дальше?")
        ]
    ],
    resize_keyboard=True
)

InlineKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Доллар", callback_data="USD"),
            InlineKeyboardButton(text="Евро", callback_data="EUR")
        ],
        [
            InlineKeyboardButton(text="Фунт", callback_data="GBP"),
            InlineKeyboardButton(text="Юань", callback_data="CNY")
        ],
        [
            InlineKeyboardButton(text="Дирхам", callback_data="AED"),
            InlineKeyboardButton(text="Лира", callback_data="TRY")
        ]

    ],
    row_width=True
)