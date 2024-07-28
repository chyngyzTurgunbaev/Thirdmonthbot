from aiogram.fsm.state import State, StatesGroup
from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import db


class RestaurantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


review_router = Router()


@review_router.callback_query(F.data == 'feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestaurantReview.name)
    await call.message.answer("Здравстуйте! Как Вас зовут?: ")


@review_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш инстаграм аккаунт: ")
    await state.set_state(RestaurantReview.instagram_username)


@review_router.message(RestaurantReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    await message.answer("Последняя дата визита: ")
    await state.set_state(RestaurantReview.visit_date)


@review_router.message(RestaurantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestaurantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Плохо')],
            [types.KeyboardButton(text='Хорошо')],
        ]
    )
    await message.answer("Оцените Еду: ", reply_markup=kb)


@review_router.message(RestaurantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await state.set_state(RestaurantReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Плохо')],
            [types.KeyboardButton(text='Хорошо')],
        ]
    )
    await message.answer("Оцените чистоту: ", reply_markup=kb)


@review_router.message(RestaurantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestaurantReview.extra_comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer('Есть ли у вас дополнительные комментарии: ', reply_markup=kb)


@review_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    db.execute(
        '''INSERT INTO reviews (tg_id,name,instagram_username,visit_date,food_rating,cleanliness_rating,extra_comments) VALUES(?,?,?,?,?,?,?)''',
        (message.from_user.id, data['name'], data['instagram_username'], data['visit_date'], data['food_rating'],
         data['cleanliness_rating'], data['extra_comments']))
    await message.answer("Ваш отзыв успешно принят!")
    await state.clear()
