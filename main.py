from handlers import notes_controller, command_handler, error_handler
from head import bot, dp, asyncio, DeleteWebhook


async def main():
    print('Я запустился')
    DeleteWebhook()
    dp.include_routers(notes_controller.notes_controller, 
                       command_handler.command_handler, 
                       error_handler.error_handler)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    