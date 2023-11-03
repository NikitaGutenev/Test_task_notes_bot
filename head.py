from imports import *
from config import TOKEN


load_dotenv()

if (tmp := os.getenv('TOKEN')) != None:
    TOKEN = tmp

bot = Bot(TOKEN)
dp = Dispatcher(storage=MemoryStorage())

notes_controller = Router(name = 'notes_controller')
error_handler = Router(name = 'error_handler')
command_handler = Router(name = 'command_handler')