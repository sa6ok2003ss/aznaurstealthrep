from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from .sqlit import get_connt_stat

#Вывод работнику его статистики
@dp.message_handler(commands=['stat'])
async def statistika(message: types.Message):
    chat_id = message.chat.id
    try:
        await bot.send_message(chat_id=message.chat.id, text= f'<b>Реферальная ссылка:\nhttps://t.me/SprintProductionBot?start={chat_id}</b>\n\n'
                                                            f'<b>Трафик:</b> {get_connt_stat(chat_id)}\n',parse_mode='html',disable_web_page_preview=True)
    except:
        pass

