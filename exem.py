import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6281199661:AAEb16wwzhS051uFWZtHgFUaoIxCvj5LeFk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Enter some text ✍️✍️")


@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text.lower()
    vowel_count = sum(text.count(vowel) for vowel in 'aeiou')

    if vowel_count > 5:
        await message.answer("There are more than 5 vowels in this message!")
        await message.delete()
    else:
        await message.answer("The number of vowel letters in this message is less than 5!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)