from db.database import User, Session, Question # Corrected import
import random

def get_user_by_telegram_id(telegram_id, session):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user
async def create_new_user(session, telegram_id):
    privilege = "user"
    new_user = User(telegram_id=telegram_id, privilege=privilege)
    try:
        session.add(new_user)
        session.commit()
        print(f"User {telegram_id} created successfully")
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {str(e)}")


def get_all_tags(session):
    return session.query(Question.tag).distinct().all()

# Функция для выбора случайного вопроса по тегу
from sqlalchemy.orm import joinedload

def get_random_question_by_tag(session, tag):
    # Получение списка вопросов, которые имеют указанный тег
    questions = session.query(Question).filter(
        Question.tags.any(name=tag)  # Здесь предполагается, что у вас есть отношение Many-to-Many или Similar
    ).all()
    
    if not questions:
        return None
    
    # Выбор случайного вопроса из списка
    return random.choice(questions)

from aiogram import types, F
from aiogram.filters import Command
from utils.config import dp
from db.database import User, Question, UserQuestion, Session
from handlers.keyboard.random_question_button import create_tags_keyboard,random_question_button, new_love_tag_F_key
import random

from db.utils import create_new_user, get_user_by_telegram_id
from utils.text import base_tag


# @dp.callback_query(F.data == "random_questions_F_key")
# async def random_questions_F_funck(callback: types.CallbackQuery):
#     await callback.message.delete()
#     session = Session() 
#     user_id = callback.message.chat.id
#     user = get_user_by_telegram_id(telegram_id=user_id, session=session)
    
#     if callback.message.chat.type == "supergroup":
#         if user:
#             await callback.message.answer("Снова привет!", reply_markup=random_question_button())
#         else:
#             await create_new_user(session=session, telegram_id=user_id)  # Добавлено await
#             await callback.message.answer("Снова привет!", reply_markup=random_question_button())
#     elif callback.message.chat.type == "private":
#         await callback.message.answer("Бот работает только в группе. Добавте его в группу")




# @dp.message(F.text.lower() == "новый вопрос")
# async def random_questions_F_funck(message: types.Message):
#     # session = Session()
    # user_telegram_id = message.chat.id

    # user = session.query(User).filter_by(telegram_id=user_telegram_id).first()
    
    # max_question_id = session.query(Question).count()
    
    # if max_question_id == 0:
    #     await message.answer("Нет доступных вопросов.")
    #     session.close()
    #     return

    # question = None
    # user_question = None

    # while not question or user_question:
    #     question_id = random.randint(1, max_question_id)
    #     # Фильтрация по тегу (если это нужно)
    #     question = session.query(Question).filter_by(question_id=question_id).first()
        
    #     if question:
    #         # Проверка, задавался ли вопрос этому пользователю
    #         user_question = session.query(UserQuestion).filter_by(user_id=user_telegram_id, question_id=question_id).first()

    # # Сохранение нового вопроса как заданного
    # user_question = UserQuestion(user_id=user_telegram_id, question_id=question_id, asked=True)
    # session.add(user_question)
    # session.commit()

    # # Вывод текста вопроса
    # await message.answer(question.question_text)
    
    # session.close()
#