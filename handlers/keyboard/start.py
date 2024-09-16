from aiogram import types

def chanel_keyboard_status():
    buttons = [
        [types.InlineKeyboardButton(text="Подписаться", url="https://t.me/macsimomg")],
        [types.InlineKeyboardButton(text="Проверка подписки", callback_data="new_start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def random_questions_F_key():
    buttons = [
        [types.InlineKeyboardButton(text="Подобрная инструкция", callback_data="help_F_key"),types.InlineKeyboardButton(text="Информация", callback_data="about_F_key")],
        [types.InlineKeyboardButton(text="Запустить", callback_data="random_questions_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def back_about_f_key():
    buttons = [
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_start_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def back_about_and_contact_f_key():
    buttons = [
        [types.InlineKeyboardButton(text="Все вопросы", url="https://t.me/macsimir"),types.InlineKeyboardButton(text="Оснвной телеграмм канал", url="https://t.me/macsimomg")],
        [types.InlineKeyboardButton(text="Назад", callback_data="back_to_start_F_key")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
