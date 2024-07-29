from config import bot, dp
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config import db

menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="drinks", callback_data="drinks")],
            [types.InlineKeyboardButton(text="first_meal", callback_data="first_meal")],
            [types.InlineKeyboardButton(text="second_meal", callback_data="second_meal")]
        ]
    )
    await message.answer("Выберите категорию", reply_markup=kb)


signal = ('drinks', 'first_meal', 'second_meal')


@menu_router.callback_query(lambda call: call.data in signal)
async def dishes(call: types.CallbackQuery):
    query = """
    SELECT * FROM dishes JOIN categories ON dishes.category_id = categories.id WHERE categories.name = ?"""
    data = db.fetch(query=query, params=(call.data,))
    for i in data:
        photo = FSInputFile(i[3])
        await call.message.answer_photo(photo=photo, caption=f'name: {i[1]}\nprice: {i[2]}')
