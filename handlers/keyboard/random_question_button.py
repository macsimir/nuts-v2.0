from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def random_question_button():
    kb = [
        [
            types.KeyboardButton(text="Новый вопрос"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
    return keyboard

# def selection_tags_button():
#     buttons = [
#         [types.InlineKeyboardButton(text="1", callback_data="random_questions_F_key")],
#         [types.InlineKeyboardButton(text="2", callback_data="help_F_key")]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Функция для формирования клавиатуры с тегами
def create_tags_keyboard(tags):
    keyboard = InlineKeyboardMarkup(row_width=2)  # Размещаем кнопки по 2 в строке

    # Создаём кнопки для каждого тега
    for tag in tags:
        button = InlineKeyboardButton(tag.tag_name, callback_data=f"tag_{tag.tag_id}")
        keyboard.add(button)
    
    return keyboard


def new_love_tag_F_key():
    buttons = [
        [types.InlineKeyboardButton(text="1", callback_data="F_1"),types.InlineKeyboardButton(text="2", callback_data="F_2"),
         types.InlineKeyboardButton(text="3", callback_data="F_3"),types.InlineKeyboardButton(text="4", callback_data="F_4"),],
        [types.InlineKeyboardButton(text="5", callback_data="F_5"),types.InlineKeyboardButton(text="6", callback_data="F_6"),
         types.InlineKeyboardButton(text="7", callback_data="F_7"),types.InlineKeyboardButton(text="8", callback_data="F_8"),]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
