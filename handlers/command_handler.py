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
    await state.update_data(note_description=message.text)
    new_note(message.text, message.from_user.id, cursor, connect)
    await message.answer(text='Ваша заметка была успешно сохранена!',
                         reply_markup=ikm_general)