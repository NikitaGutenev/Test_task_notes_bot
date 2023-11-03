from head import command_handler, bot, cursor, connect, \
                    Command, Message, FSMContext,  CallbackQuery, FSMContext, StatesGroup, State, \
                    new_note, get_notes, del_note, dp, F
from keyboards.inline_keyboards.inline_keyboard import ikm_general
from keyboards.inline_keyboards.callback import *


@command_handler.message(Command('start'))
async def start(message: Message):
    await bot.send_photo(chat_id=message.from_user.id,
                            photo="https://avatars.mds.yandex.net/i?id=707848d0844ae92dfe07e7b92029273c130f9965-10918904-images-thumbs&n=13",
                            caption=f'Привет, {message.from_user.full_name}!\n' + \
                                    'Что хочешь сделать со своими заметками?👇',
                            reply_markup=ikm_general)


@command_handler.message(NoteStates.add_note)
async def add_note(message: Message, state: FSMContext):
    new_note(message.text, message.from_user.id, cursor, connect)
    await message.answer(text='Ваша заметка была успешно сохранена!',
                         reply_markup=ikm_general)
    await state.clear()
    

@command_handler.message(NoteStates.del_note)
async def add_note(message: Message, state: FSMContext):
    if message.text.isdigit():
        await bot.send_message(text=f"Точно удалить заметку с ID: {message.text}?",
                                    chat_id=message.from_user.id,
                                    reply_markup=InlineKeyboardBuilder([[
                                                InlineKeyboardButton(text="Да", callback_data="del"+"yes"+message.text),
                                                InlineKeyboardButton(text="Нет", callback_data="del"+"no "+message.text)]]).as_markup())
        await state.clear()
    elif message.text == "exit":
        await bot.send_message(chat_id=message.from_user.id,
                               text="Заметка не удалена",
                               reply_markup=ikm_general)
        await state.clear()
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Это не ID. Попробуйте снова или напишите exit")
        