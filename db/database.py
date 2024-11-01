from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    privilege = Column(String)

    @classmethod
    def telegram_id_exists(cls, session, telegram_id):
        return session.query(cls).filter(cls.telegram_id == telegram_id).first() is not None


class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(Text)
    tag_question = Column(Integer, ForeignKey("tag.tag_id"))

    tag = relationship("Tag")

class UserQuestion(Base):
    __tablename__ = 'user_questions'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'), primary_key=True)
    asked = Column(Boolean, default=False)

class Tag(Base):
    __tablename__ = "tag"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_text = Column(Text)





engine = create_engine('sqlite:///DATEBASE.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_user_by_telegram_id(session, telegram_id):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user

if __name__ == "__main__":
    # Создаем сессию для взаимодействия с БД
    session = Session()

    try:
        # Проверяем, создана ли таблица users
        users_exist = session.query(User).first()
        if users_exist:
            print("Таблица users создана.")
        else:
            print("Таблица users не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы users: {e}")
    
    try:
        # Проверяем, создана ли таблица questions
        questions_exist = session.query(Question).first()
        if questions_exist:
            print("Таблица questions создана.")
        else:
            print("Таблица questions не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы questions: {e}")

    try:
        # Проверяем, создана ли таблица user_questions
        user_questions_exist = session.query(UserQuestion).first()
        if user_questions_exist:
            print("Таблица user_questions создана.")
        else:
            print("Таблица user_questions не создана.")
    except Exception as e:
        print(f"Ошибка при проверке таблицы user_questions: {e}")

    # Пример использования функции get_user`_by_telegram_id
    
