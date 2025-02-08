from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

bot = Bot('8101193115:AAFwZ6wJTlrvolPdceh0paNL1UP2NazCMlw')

dp = Dispatcher()

@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text='Привет! Это обычный бот в разработке.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())