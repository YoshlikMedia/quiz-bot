from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from keyboards.default.menuKeyboard import menu
from keyboards.inline.choose_subject import Subject, Curriculum, Level
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(text=text['start_text'].format(message.from_user.full_name), reply_markup=menu)
