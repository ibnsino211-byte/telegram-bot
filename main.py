import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8671853037:AAF9MgjXiB53fuy_bJe2m2N4yxfS1Rl_SGU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Bot ishlayapti 🚀")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
