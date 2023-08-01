import security.bucket
import time 

async def procces_dox(dp):
    @dp.callback_query_handler(text_startswith='number')
    async def search(call: security.bucket.types.CallbackQuery):
        await call.answer()
        text = '''
🎃 Отправьте данные такие как 🎃
🔍 Номер телефона 
🔍 Почта 
🔍 Имя
🔍 Страничка в vk 
🔍 Страничка в Instagram
'''
        await call.message.edit_text(text)


import security.bucket
import asyncio

async def procces_dox(dp):
    @dp.message_handler(commands='dox')
    async def dox(message: security.bucket.types.Message):
        text = 'Отправьте текстовые данные, которые вы хотите найти'
        await message.answer(text)

    @dp.message_handler(content_types='text')
    async def handle_text(message: security.bucket.types.Message):
        search_text = message.text
        file_path = 'dox.txt'
        results = await find_data_by_text(file_path, search_text)

        if results:
            text = "Данные которые были найдены 📝:\n" + "\n".join(results)
        else:
            text = "Ничего не найдено."

        # Отправка различных статусов во время выполнения операции
        sent_message = await message.answer('Поиск данных …')
        await asyncio.sleep(1)
        await sent_message.edit_text('Проверка в базе данных …')
        await asyncio.sleep(1)
        await sent_message.edit_text('bzzzzzzzz')
        await asyncio.sleep(1)
        await sent_message.edit_text(text)

async def find_data_by_text(file_path, search_text):
    try:
        matching_lines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if search_text.lower() in line.lower():
                    matching_lines.append(line.strip())

        return matching_lines
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None