from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton






clava = InlineKeyboardMarkup(row_width=1)
btnreturnmenu=InlineKeyboardButton(text='вернуться в меню', callback_data='returnMenu')
buy_pear1 = InlineKeyboardButton(text="какой жанр хочешь почитать?👀", callback_data="топ")
buy_pear13=InlineKeyboardButton(text="манхвы 18+", callback_data="18+")
buy_pear15=InlineKeyboardButton(text="управление подпиской", callback_data="subscribemanagment")
zakladki=InlineKeyboardButton(text="Закладки", callback_data="Myzakladki")
film = InlineKeyboardButton(text="testik", callback_data="film")
clava.insert(buy_pear1)
clava.insert(zakladki)
clava.insert(film)
#clava.insert(buy_pear13)
#clava.insert(buy_pear15)


filmClava=InlineKeyboardMarkup(row_width=1)
tvoeImya=InlineKeyboardButton(text="Твое имя", callback_data="tvoeImya")
dityaShud=InlineKeyboardButton(text="Дитя чудовища", callback_data="dityaShud")
KRDInfinityPoezd=InlineKeyboardButton(text="Клинок, рассекающий демонов: Бесконечный поезд", callback_data="KRDInfinityPoezd")
filmClava.insert(tvoeImya)
filmClava.insert(dityaShud)
filmClava.insert(KRDInfinityPoezd)


watchFilm=InlineKeyboardMarkup(row_width=1)
watch=InlineKeyboardButton(text="Смотреть", callback_data="watch")
watchFilm.insert(watch)
watchFilm.insert(btnreturnmenu)

clavaChangeState=InlineKeyboardMarkup(row_width=1)
buy_pear5 = InlineKeyboardButton(text="начать читать с начала", callback_data="начать с начала")
buy_pear6 = InlineKeyboardButton(text="я знаю с какой главы хочу читать", callback_data="поиск главы")
subscribe = InlineKeyboardButton(text="подписаться на выход новой главы", callback_data="subscribeNew")
download=InlineKeyboardButton(text="прислать все главы сразу", callback_data="download")
zak = InlineKeyboardButton(text= "Добавить в закладки", callback_data="addToZakladki")
delzak = InlineKeyboardButton(text= "Убрать из закладок", callback_data="DeleteZakladki")
clavaChangeState.insert(buy_pear5)
clavaChangeState.insert(buy_pear6)
clavaChangeState.insert(subscribe)
clavaChangeState.insert(download)
clavaChangeState.insert(zak)
clavaChangeState.insert(delzak)
clavaChangeState.insert(btnreturnmenu)



nextchapter=InlineKeyboardMarkup(row_width=1)
buy_pear7 = InlineKeyboardButton(text="next", callback_data="next")
buy_pear8 = InlineKeyboardButton(text="найти другую главу", callback_data="поиск главы")
nextchapter.insert(buy_pear7)
nextchapter.insert(buy_pear8)
nextchapter.insert(btnreturnmenu)



checkSubm=InlineKeyboardMarkup(row_width=1)
btnurlchannel= InlineKeyboardButton(text='подписаться', url='https://t.me/manhwastorage')
btndonesub=InlineKeyboardButton(text='я подписался', callback_data='саб')
checkSubm.insert(btnurlchannel)
checkSubm.insert(btndonesub)


cancelsub=InlineKeyboardMarkup(row_width=1)
btncancel=InlineKeyboardButton(text="отменить?", callback_data="cancelmanhwasub")
cancelsub.insert(btncancel)
cancelsub.insert(btnreturnmenu)



returN=InlineKeyboardMarkup(row_width=1)
returN.insert(btnreturnmenu)
