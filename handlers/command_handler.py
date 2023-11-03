from head import command_handler, Command, Message, bot

@command_handler.message(Command('start'))
async def start(message: Message):
    await bot.send_photo(chat_id=message.from_user.id,
                            photo='',
                            caption=f'Привет, {message.from_user.full_name}!\n' + \
                                    'Что хочешь сделать со своими заметками?👇',
                            reply_markup=)