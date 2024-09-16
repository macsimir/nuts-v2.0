import logging
import asyncio
from utils.config import dp, bot

logging.basicConfig(level=logging.INFO)

async def main():
    from handlers.users import start, random_question # импортируем все обработчики
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен и готов к работе")
    asyncio.run(main())


# echo "# nuts-v2.0" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/macsimir/nuts-v2.0.git
# git push -u origin main