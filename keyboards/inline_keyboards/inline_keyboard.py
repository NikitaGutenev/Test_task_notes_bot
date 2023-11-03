from head import InlineKeyboardButton, InlineKeyboardBuilder


del_button = InlineKeyboardButton(text="Удалить заметку", callback_data="general_del_note")
get_button = InlineKeyboardButton(text="Показать список заметок", callback_data="general_get_notes")
new_button = InlineKeyboardButton(text="Добавить новую заметку", callback_data="general_add_note")


ikm_general = InlineKeyboardBuilder([[get_button,
                                    new_button,
                                    del_button]]
                                    ).adjust(1).as_markup()


ikm_note = InlineKeyboardBuilder([[
    get_button,
    new_button,
    InlineKeyboardButton(text="Удалить заметку", callback_data="del_note_now")
]])


ikm_yes_no = InlineKeyboardBuilder([[
    InlineKeyboardButton(text="Да", callback_data="yes"),
    InlineKeyboardButton(text="Нет", callback_data="no")
]])