import security.bucket
import text.search_text
import inlinemenu.back_menu


async def procces_search_handlers(dp):
    @dp.callback_query_handler(text_startswith='search')
    async def search(call: security.bucket.types.CallbackQuery):
        await call.answer()
        await call.message.edit_text(text.search_text.message_search,reply_markup=inlinemenu.back_menu.back)
        procces_search_handlers(dp)