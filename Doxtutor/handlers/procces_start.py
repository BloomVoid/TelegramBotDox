import security.bucket
import inlinemenu.start_menu
import text.strat_txt
import image.image_for_start


async def procces_start_handlers(dp):
    @dp.message_handler(commands='start')
    async def start(message: security.bucket.types.Message):
        chat = message.chat.id
        await dp.bot.send_message(chat,image.image_for_start.start_image)
        await message.answer(text.strat_txt.message_start,reply_markup=inlinemenu.start_menu.start_menu)



    @dp.callback_query_handler(text_startswith="start")
    async def next_page(call: security.bucket.types.CallbackQuery):
        await call.answer()
        await call.message.edit_text(text.strat_txt.message_start,reply_markup=inlinemenu.start_menu.start_menu)  
        procces_start_handlers(dp)

