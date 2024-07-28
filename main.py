import asyncio
from config import bot, dp
from handlers.recipes import recipe_router
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router
from config import db
async def main():
    db.create_table()
    dp.include_router(start_router)
    dp.include_router(recipe_router)
    dp.include_router(my_info_router)
    dp.include_router(dishes_router)
    dp.include_router(review_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
