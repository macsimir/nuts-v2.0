from aiogram import types, F
from aiogram.filters import Command
from utils.config import dp
from db.database import User, Question, UserQuestion, Session, Tag
import random

from db.utils import create_new_user, get_user_by_telegram_id
from handlers.keyboard.random_question_button import random_question_button
# Функция для получения случайного тега
def get_random_tag(session):
    tag_count = session.query(Tag).count()
    if tag_count == 0:
        return None
    random_tag_id = random.randint(1, tag_count)
    return session.query(Tag).filter_by(tag_id=random_tag_id).first()


@dp.callback_query(F.data == "random_questions_F_key")
async def random_questions_F_funck(callback: types.CallbackQuery):
    await callback.message.delete()
    session = Session() 
    user_id = callback.message.chat.id
    user = get_user_by_telegram_id(telegram_id=user_id, session=session)
    
    
    if callback.message.chat.type == "private":
        await callback.message.answer("Бот работает только в группе. Добавте его в группу")
    else: 
        if user:
            await callback.message.answer("Снова привет! Напоминаю что для того чтобы начать общаться нажимай кнопку 'Новый вопрос'", reply_markup=random_question_button())
        else:
            await create_new_user(session=session, telegram_id=user_id)  # Добавлено await
            await callback.message.answer('Привет, для того чтобы начать нажмите кнопку "Новый вопрос"', reply_markup=random_question_button())




@dp.message(F.text.casefold() == "новый вопрос")
async def random_questions_F_funck(message: types.Message):
    session = Session() 
    user_id = message.chat.id
    user = get_user_by_telegram_id(telegram_id=user_id, session=session)
    if user:
        print(2)
        # Получение случайного тега
        random_tag = get_random_tag(session)
        if random_tag:
            print(3)
            tag_name = random_tag.tag_text
            questions = session.query(Question).filter_by(tag_question=random_tag.tag_id).all()
            if questions:
                print(4)
                # Выбор вопроса, который ещё не был задан пользователю
                asked_question_ids = session.query(UserQuestion.question_id).filter_by(user_id=user_id, asked=True).all()
                asked_question_ids = {id[0] for id in asked_question_ids}
                
                available_questions = [q for q in questions if q.question_id not in asked_question_ids]
                
                if available_questions:
                    print(5)
                    question = random.choice(available_questions)
                    # Сохранение нового вопроса как заданного
                    user_question = UserQuestion(user_id=user_id, question_id=question.question_id, asked=True)
                    session.add(user_question)
                    session.commit()
                    
                    # Вывод вопроса с тегом
                    await message.answer(f"Тег: {tag_name}\nВопрос: {question.question_text}")
                else:
                    await message.answer("Все вопросы с этим тегом уже были заданы.")
            else:
                await message.answer("Нет доступных вопросов с этим тегом.")
        else:
            await message.answer("Нет доступных тегов.")
    else:
        await create_new_user(session=session, telegram_id=user_id)  # Добавлено await
        await message.answer("Снова привет!")

    session.close()