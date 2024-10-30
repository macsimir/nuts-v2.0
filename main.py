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
