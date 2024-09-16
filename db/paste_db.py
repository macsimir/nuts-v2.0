from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from database import Tag,Question

Base = declarative_base()

# class Tag(Base):
#     __tablename__ = "tag"
#     tag_id = Column(Integer, primary_key=True, autoincrement=True)
#     tag_text = Column(Text)

# class Question(Base):
#     __tablename__ = 'questions'
#     question_id = Column(Integer, primary_key=True, autoincrement=True)
#     question_text = Column(Text)
#     tag_question = Column(Integer, ForeignKey("tag.tag_id"))

#     tag = relationship("Tag")

# Установка соединения с базой данных
engine = create_engine('sqlite:///DATEBASE.db')  # Укажите путь к вашей базе данных
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Список вопросов
questions = [
    "Мне очень нравится твой (любой предмет одежды). Откуда он?",
    "Ты больше любишь чай или кофе?",
    "Что ты любишь есть на завтрак?",
    "Что ты сейчас читаешь?",
    "От какого сериала у тебя не получалось оторваться?",
    "Какой сериал ты смотришь, когда хочешь расслабиться?",
    "Какой концерт был самым ярким в твоей жизни?",
    "Какие подкасты ты слушаешь?",
    "У тебя есть любимый вид спорта?",
    "Какой твой любимый праздник?"
]

# Уникальные теги для каждого вопроса
tags = [
    " Карьера",
"Хобби и увлечения",
"Путешествия",
"Книги и литература",
"Фильмы и сериалы",
"Спорт и физическая активность",
"Музыка",
"Технологии",
"Образование",
"Ценности и убеждения",
"Семья",
"Здоровье и уход за собой",
"Социальные сети",
"Будущее и мечты",
"Личные достижения",
"Экология и окружающая среда",
"Философия и мысли",
"Творчество",
]

# Добавляем теги
tag_objects = [Tag(tag_text=tag) for tag in tags]
session.add_all(tag_objects)
session.commit()

# Вставка вопросов в таблицу questions
# for i, question_text in enumerate(questions):
#     tag_id = tag_objects[i].tag_id
#     new_question = Question(question_text=question_text, tag_question=tag_id)
#     session.add(new_question)

# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
