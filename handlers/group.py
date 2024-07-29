from config import bot
from aiogram import types, Router
from aiogram.filters import Command
from datetime import datetime, timedelta

group_router = Router()
BAD_WORDS = ("дурак", "тупой", "ненормальный", "nigga")


@group_router.message(Command('ban', prefix="!"))
async def ban_user(message: types.Message):
    reply = message.reply_to_message
    if reply:
        author = reply.from_user.id
        until_date = datetime.utcnow() + timedelta(seconds=90)
        await bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=author,
            until_date=until_date
        )


@group_router.message()
async def echo(message: types.Message):
    for word in message.text.split():
        if word in BAD_WORDS:
            await message.delete()
            await message.answer(
                f"{message.from_user.first_name},Вы использовали плохое слово"

            )
            author = message.from_user.id
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=author,
                until_date=timedelta(seconds=90)

            )
