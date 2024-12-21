import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '7740385507:AAEK9ZtXuoEIcbpyvGN5-Rr-aco9zjlyNa4'
memory_storage = MemoryStorage()
print(1)
bot = Bot(token=TOKEN,parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)
print(2)