from aiogram import types, F
from aiogram.filters import Command
from utils.config import bot, dp
from handlers.keyboard.start import chanel_keyboard_status, random_questions_F_key, back_about_f_key, back_about_and_contact_f_key

text_to_start_command = '''Здравствуйте! Я — Орешек, ваш помощник, который поможет вам начать разговор и сделает его более увлекательным. 🌰

Выберите режим работы "Случайные вопросы" 🎲, чтобы получить случайный вопрос, который поможет вам начать беседу.

Чтобы начать общение, добавьте бота в вашу группу, в которой вы собираетесь общаться. 💬

Если у вас возникли вопросы, подробную инструкцию можно найти, нажав на кнопку "Подробная инструкция" 📜.

Если хотите узнать всю основную информацию о боте, нажмите на кнопку "Информация" ℹ️.'''

@dp.message(Command("start"))
async def start_command(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=message.from_user.id)
    if user_channel_status.status != 'left':
        await message.answer(text_to_start_command, reply_markup=random_questions_F_key())
    else:
        await message.answer('Для начала подпишись на наш канал', reply_markup=chanel_keyboard_status())


@dp.callback_query(F.data == "new_start")
async def new_start_funck_key(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=callback.from_user.id)
    if user_channel_status.status != 'left':
        await callback.message.answer('Спасибо за подписку!')
        await callback.message.answer(text_to_start_command)
    else:
        await callback.message.answer('Ты все еще не подписался')


@dp.callback_query(F.data == "help_F_key")
async def help_command(callback: types.CallbackQuery):

    await callback.message.answer('''Чтобы начать использовать бота, выполните следующие шаги:
    1.Создайте группу 👥
    2.Добавьте туда своего друга 👦
    3.Затем добавьте бота 🤖
    4.Сделайте его администратором и предоставьте доступ к чтению сообщений 🛠️
    5.После этого нажмите команду "Запустить" 🚀

''', reply_markup=back_about_f_key())

@dp.callback_query(F.data == "back_to_start_F_key")
async def back_to_start_F_key_command(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='@macsimomg', user_id=callback.message.from_user.id)
    if user_channel_status.status != 'left':
        await callback.message.answer(text_to_start_command, reply_markup=random_questions_F_key())
    else:
        await callback.message.answer('Для начала подпишись на наш канал', reply_markup=chanel_keyboard_status())

@dp.callback_query(F.data == "about_F_key")
async def about_F_key_command(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('''Орешек — это уникальный бот, созданный специально для того, чтобы сделать ваше онлайн-общение более интересным и увлекательным. 🌐

В жизни бывают моменты, когда хочется начать знакомство с кем-то новым с самого начала, узнать его поближе и поделиться своими мыслями и чувствами. Наш бот как раз для таких случаев! 🗣️

С помощью Орешка вы сможете не только ответить на забавные и необычные вопросы, которые разбудят ваше любопытство , но и погрузиться в более глубокие и философские обсуждения о смысле жизни, мечтах и целях 🤔.

Мы надеемся, что общение с нашим ботом станет для вас интересным и познавательным опытом!

Контактные данные:''', reply_markup=back_about_and_contact_f_key())
