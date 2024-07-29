from aiogram import types, Router
from aiogram.filters import Command

my_info_router = Router()


@my_info_router.message(Command('my_info'))
async def my_info(message: types.Message):
    await message.answer(f'Name: {message.from_user.first_name}\n'
                         f'id: {message.from_user.id}')
