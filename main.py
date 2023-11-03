from handlers import command_handler
from head import bot, dp, asyncio, DeleteWebhook


async def main():
    print('Я запустился')
    DeleteWebhook()
    dp.include_router(command_handler.command_handler)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    