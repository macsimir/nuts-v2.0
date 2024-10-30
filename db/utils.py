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

