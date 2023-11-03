from head import command_handler, notes_controller, error_handler, cursor, connect, bot, \
                F, CallbackQuery, FSMContext, StatesGroup, State, InlineKeyboardBuilder, InlineKeyboardButton, \
                get_notes, del_note
from keyboards.inline_keyboards.inline_keyboard import ikm_note, ikm_general

class NoteStates(StatesGroup):
    add_note = State()


@command_handler.callback_query(F.data[:2] == "ID")
async def get_my_note(callback: CallbackQuery):
    data = callback.data[2:]
    await callback.answer(text="Поиск вашей заметки...")
    note = get_notes(data, cursor, count=1)[0]
    text = f"""
ID:{note[0]}
Last edit: {note[2]}

{note[1]}"""
    await bot.send_message(chat_id=callback.from_user.id,
                           text=text,
                           reply_markup=ikm_note)


@command_handler.callback_query()
async def command_query_handler(callback: CallbackQuery, state: FSMContext):
    data = callback.data
    match data:
        case "general_get_notes":
            await callback.answer(text="")
            notes = get_notes(callback.from_user.id, cursor)
            if notes:
                markup = InlineKeyboardBuilder()
                for i in notes:
                    markup.add(InlineKeyboardButton(text=i[1][:12]+"...", callback_data="ID"+str(i[0])))
                    markup.adjust(1)
                markup = markup.as_markup()
                text = "Ваши заметочки:"
            else:
                text = "У вас еще нет заметок"
                markup = None
            await bot.send_message(chat_id=callback.from_user.id,
                                   text = text,
                                   reply_markup=markup)
                
        case "general_add_note":
            await callback.answer(text="Введите ваше сообщение:")
            await state.set_state(NoteStates.add_note)

        case "general_del_note":
            await bot.edit_message_text(text="Точно удалить?",
                                        chat_id=callback.from_user.id,
                                        message_id=callback.message.id,
                                        reply_markup=)
            await callback.answer(text="Ваша заметка удалена")

        case "del_note_now":
            pass
