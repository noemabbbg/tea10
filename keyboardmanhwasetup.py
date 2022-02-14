from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
btnreturnmenu=InlineKeyboardButton(text='вернуться в меню', callback_data='returnMenu')




clava18=InlineKeyboardMarkup(row_width=5)
buy_pear2 = InlineKeyboardButton(text="убийца героев", callback_data="HeroKiller")
hent1 = InlineKeyboardButton(text="я забыл название но оно работает", callback_data="хент1")
clava18.insert(hent1)

clavaTOP = InlineKeyboardMarkup(row_width=1)
buy_pear3 = InlineKeyboardButton(text="поднятие уровня в одиночку", callback_data="Solo")
buy_pear4 = InlineKeyboardButton(text="Большая жизнь", callback_data="BigLife")
buy_pear11 = InlineKeyboardButton(text="убийца героев", callback_data="HeroKiller")
buy_pear12 = InlineKeyboardButton(text="Элисед", callback_data="Eliced")
buy_pear13 = InlineKeyboardButton(text="Так я женился на антифанатке", callback_data="antifanatka")
buy_pear14 = InlineKeyboardButton(text="Королева со скальпелем", callback_data="queenwithscalpel")
SCB=InlineKeyboardButton(text="SuicideBoy", callback_data="SuicideBoy")
box = InlineKeyboardButton(text="Боксер", callback_data="Boxer")
Bastard = InlineKeyboardButton(text="Cволочь", callback_data="Bastard")
princ = InlineKeyboardButton(text="Однажды я стала принцессой", callback_data="odnazhprinc")
chertovka = InlineKeyboardButton(text="Берегись этой чертовки!", callback_data="chertovka")
chizel= InlineKeyboardButton(text="Кровь мадам Жизель", callback_data="chizel")
Born= InlineKeyboardButton(text="Прирожденный наёмник", callback_data="Born")

clavaTOP.insert(box)
clavaTOP.insert(Bastard)
clavaTOP.insert(SCB)
clavaTOP.insert(buy_pear12)
clavaTOP.insert(buy_pear13)
clavaTOP.insert(buy_pear14)
clavaTOP.insert(princ)
clavaTOP.insert(chertovka)
clavaTOP.insert(chizel)
clavaTOP.insert(Born)
clavaTOP.insert(btnreturnmenu)