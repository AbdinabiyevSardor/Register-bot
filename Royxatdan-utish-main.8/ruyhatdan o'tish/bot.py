import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,FSInputFile
from states import Form
from aiogram.fsm.context import FSMContext
import re

ADMIN = YOUR ID
TOKEN = "YOUR_TOKEN"
bot = Bot(TOKEN,parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext):
    
    await state.set_state(Form.first_name)
    await message.answer(text="Assalomu alaykum.!!!")
    await message.answer(text=" Sifat o'quv kursida o'qimoqchi bo'lsangiz ro'yxatdan o'tish uchun ismingizni kiriting!!!")
    
    
@dp.message(F.text,Form.first_name)  
async def first_name_register(message:Message,state:FSMContext):
    ism = message.text
    await state.update_data(first_name=ism)
    await state.set_state(Form.last_name)
    
    await message.answer(text="Familiyangizni kiriting")

@dp.message(F.text,Form.last_name)
async def last_name_register(message:Message,state:FSMContext):
    familiya = message.text
    await state.update_data(last_name=familiya)
    await state.set_state(Form.phone_number)
    
    await message.answer(text="Telefon nomeringizni kiriting")
    await message.answer(text="Iltimos +998 bilan boshlang!!!")
    
@dp.message(F.text,Form.phone_number)
async def last_name_register(message:Message,state:FSMContext):
    nomer = message.text
    pattern = re.compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
    if pattern.match(nomer):
        await state.update_data(phone_number=nomer)
        await state.set_state(Form.country)
        await message.answer(text="Qaysi davlatda yashaysiz???")    
    else:
        await message.answer(text="Telefon nomeringiz noto'g'ri qayta kiriting???")
        
    
    
    
@dp.message(F.text,Form.country)
async def last_name_register(message:Message,state:FSMContext):
    davlat = message.text
    await state.update_data(country=davlat)
    await state.set_state(Form.year)
    
    await message.answer(text="Yilingizni kiriting!")

    
@dp.message(F.text,Form.year)
async def last_name_register(message:Message,state:FSMContext):
    yosh = message.text
    try:
        await state.update_data(age=2024 - int(yosh))
        await message.answer(text=f"Yoshingiz: {2024 - int(yosh)}")
        await state.set_state(Form.work)

        await message.answer(text="Qayerda ishlaysiz kiriting???")

    except:
        await message.answer(text="Iltimos, haqiqiy tug'ilgan yilingizni kiriting!!!")
    
@dp.message(F.text,Form.work)
async def last_name_register(message:Message,state:FSMContext):
    ish_joy = message.text
    await state.update_data(work=ish_joy)
    await state.set_state(Form.address)
    await message.answer(text="Manzilingizni kiriting???")

    
    
    

@dp.message(F.text,Form.address)
async def address_register(message:Message,state:FSMContext):
    adres = message.text
    await state.update_data(address=adres)
    data = await state.get_data()
    first_name = str(data.get("first_name")).lower().capitalize()
    last_name = str(data.get("last_name")).lower().capitalize()
    phone_number = data.get("phone_number")
    country = data.get("country")
    age = data.get("age")
    work = data.get("work")
    address = data.get("address")
    text = f"Yangi foydalanuvchi:\nIsmi>>> {first_name}\nFamiliyasi>>> {last_name}\nYoshi>>> {age}\nTelefon raqami>>> {phone_number}\nIshlash_joyi>>> {work}Davlati>>> {country}\nManzili>>> {address}"
    await bot.send_message(chat_id=ADMIN, text=text)
    
    
    await state.clear()
    
    
    
    
    await message.answer(text="Siz ro'yxatdan o'tdingiz!!!")


    
    
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
