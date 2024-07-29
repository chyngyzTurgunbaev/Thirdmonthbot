from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile

dishes_router = Router()


@dishes_router.message(F.text == 'напитки')
async def drinks(message: types.Message):
    photo = FSInputFile("images/cola.jpeg")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption="Coca-Cola"
    )


@dishes_router.message(F.text == 'блюдо')
async def dishes(message: types.Message):
    photo = FSInputFile("images/kuurdak.jpeg")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption="kuurdak"
    )
