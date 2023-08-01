import security.bucket
import security.config
from concurrent.futures.thread import _shutdown
from handlers.procces_start import procces_start_handlers
from handlers.procces_search import procces_search_handlers
from handlers.procces_info import procces_info_handlers
from handlers.procces_doxbin import procces_dox,find_data_by_text

bot = security.bucket.Bot(token=security.config.TOKEN)
storage = security.bucket.MemoryStorage()
main = security.bucket.Dispatcher(bot, storage=storage)

security.bucket.logging.basicConfig(level=security.bucket.logging.INFO)
  
async def on_startup(dp):
    await procces_start_handlers(dp) 
    await procces_search_handlers(dp)
    await procces_info_handlers(dp)
    await procces_dox(dp)
    
 
if __name__ == "__main__":
    security.bucket.executor.start_polling(main, on_startup=on_startup, on_shutdown=_shutdown)
  