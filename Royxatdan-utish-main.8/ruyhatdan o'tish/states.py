from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    country = State()
    year = State()
    work = State()
    address = State()

    






