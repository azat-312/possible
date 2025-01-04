from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging

token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
Admins=[902814307 ,]
async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,text='бот включен')
@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    await bot .send_message(chat_id=message.from_user.id,
                            text=F'Hello {message.from_user.first_name}!\n'
                                f'твой телеграм ID - {message.from_user.id}\n' )
    with open(photo_path, 'rb')as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='это мем')
        await message.answer_photo(photo=photo,caption='Мем')
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)

