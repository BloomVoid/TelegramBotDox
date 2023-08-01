import security.bucket
import inlinemenu.back_menu


async def procces_info_handlers(dp):
    @dp.callback_query_handler(text_startswith='info')
    async def search(call: security.bucket.types.CallbackQuery):
        text=f'''
🆔: {call.message.chat.id}
🎃: {call.message.chat.first_name}
🙉: {call.message.chat.username}
📃: {call.message.chat.photo}
'''
        await call.answer()
        await call.message.edit_text(text,reply_markup=inlinemenu.back_menu.back)
        procces_info_handlers(dp)