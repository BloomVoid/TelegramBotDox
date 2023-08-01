import security.bucket

start_menu = security.bucket.InlineKeyboardMarkup()
search = security.bucket.InlineKeyboardButton(text='🔍 Поиск',callback_data='search')
info = security.bucket.InlineKeyboardButton(text='📋 Информация ',callback_data='info')
shop = security.bucket.InlineKeyboardButton(text='🛍️ Магазин ',callback_data='shop')
settings = security.bucket.InlineKeyboardButton(text='⚙️ Настройки ',callback_data='settings')
menu = security.bucket.InlineKeyboardButton(text='🧳 Меню',callback_data='menu')
start_menu.row(search,info,shop)
start_menu.row(settings,menu)

