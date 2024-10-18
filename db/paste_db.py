from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Tag  # Импортируйте ваши модели

# Создайте подключение к базе данных
engine = create_engine('sqlite:///db/DATEBASE.db')  # Замените на вашу строку подключения
Base.metadata.create_all(engine)  # Создайте все таблицы, если они еще не созданы

Session = sessionmaker(bind=engine)
session = Session()

# Список тегов для добавления
tags_list = [
    "Увлечения",
    "Карьера",
    "Мечты",
    "Работа",
    "Путешествия",
    "Семья",
    "Образование",
    "Культура",
    "Дружба",
    "Любовь",    
]

# Создание и добавление тегов в сессию
for tag_text in tags_list:
    tag = Tag(tag_text=tag_text)
    session.add(tag)

# Сохраните изменения в базе данных
session.commit()

# Закройте сессию
session.close()
