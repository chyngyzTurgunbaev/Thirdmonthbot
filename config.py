from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
from database.database import Database

load_dotenv()
debug = getenv("DEBUG", 0)
if not debug:
    print("bot запускается на сервере")
    from aiogram.client.session.base import AiohttpSession

    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("TOKEN"), session=session)
else:
    print("bot запущен на компе")
    bot = Bot(token=getenv("TOKEN"))

token = getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
db = Database('cafe.sqlite3')
