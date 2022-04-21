from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
btnreturnmenu=InlineKeyboardButton(text='вернуться в меню↩️', callback_data='returnMenu')



clavaTOP = InlineKeyboardMarkup(row_width=1)
buy_pear12 = InlineKeyboardButton(text="Элисед🔥", callback_data="Eliced") 
buy_pear13 = InlineKeyboardButton(text="Так я женился на антифанатке", callback_data="antifanatka")
buy_pear14 = InlineKeyboardButton(text="Королева со скальпелем", callback_data="queenwithscalpel")
SCB=InlineKeyboardButton(text="SuicideBoy", callback_data="SuicideBoy")
box = InlineKeyboardButton(text="Боксер🔥", callback_data="Boxer")
Bastard = InlineKeyboardButton(text="Cволочь🔥🔥", callback_data="Bastard")
princ = InlineKeyboardButton(text="Однажды я стала принцессой", callback_data="odnazhprinc")
chertovka = InlineKeyboardButton(text="Берегись этой чертовки!", callback_data="chertovka")
chizel= InlineKeyboardButton(text="Кровь мадам Жизель", callback_data="chizel")
Born= InlineKeyboardButton(text="Прирожденный наёмник", callback_data="Born")
Annara=InlineKeyboardButton(text="Аннарасуманара🔥", callback_data="Annara")
SweetHome=InlineKeyboardButton(text="Милый дом🔥", callback_data="SweetHome")
KRD=InlineKeyboardButton(text="Клинок, рассекающий демонов🔥", callback_data="KRD")
MyfirstLove=InlineKeyboardButton(text="Моя первая любовь — сплошная неприятность", callback_data="MyfirstLove")
LoveYourEnemy=InlineKeyboardButton(text="Люби своего врага🔥", callback_data="LoveYourEnemy")
Svinarnik=InlineKeyboardButton(text="Svinarnik(18+)🔥", callback_data="Svinarnik")   #в триллер 
Vetrolom=InlineKeyboardButton(text="Ветролом🔥", callback_data="Vetrolom")    # в экшн
VosvrashenieMax=InlineKeyboardButton(text="Возвращение героя максимального уровня", callback_data="VosvrashenieMax")
VtorayShiznZlodeyki=InlineKeyboardButton(text="Вторая жизнь злодейки", callback_data="VtorayShiznZlodeyki")# v romantik
MirKot=InlineKeyboardButton(text="Мир, управляемый котами", callback_data="MirKot") # v romantik
tridvedma=InlineKeyboardButton(text="Тридцатилетняя ведьма", callback_data="tridvedma") # v romantik
charstvoboevixisk=InlineKeyboardButton(text="Царство боевых искусств", callback_data="charstvoboevixisk")
zlodeykaperevnulac=InlineKeyboardButton(text="Злодейка, перевершнувшая песочные часы", callback_data="zlodeykaperevnulac")
kusatludeiinepravilno=InlineKeyboardButton(text="Кусать людей так неправильно🔥", callback_data="kusatludeiinepravilno")
svyatidol=InlineKeyboardButton(text="Священный айдол", callback_data="svyatidol")
yastalamateriugg=InlineKeyboardButton(text="Я стала матерью главного героя", callback_data="yastalamateriugg")
ReinkarVoen=InlineKeyboardButton(text="Реинкарнация военного🔥", callback_data="ReinkarVoen")
TokyoGhoul=InlineKeyboardButton(text="Токийский гуль", callback_data="TokyoGhoul")
TokyoGhoulRE=InlineKeyboardButton(text="Токийский гуль: Перерождение", callback_data="TokyoGhoulRE")
SaveMe=InlineKeyboardButton(text="Спаси меня", callback_data="SaveMe")
NeudPravda=InlineKeyboardButton(text="Неудобная правда🔥🔥🔥", callback_data="NeudPravda")
Zero=InlineKeyboardButton(text='У вас пока нет ничего в закладках', callback_data='returnMenu') 
EPTA = [Zero, Zero,Zero,Zero, buy_pear12, 
SCB, 
box, 
Bastard, 
buy_pear13, 
buy_pear14, 
princ, 
chertovka, 
chizel, 
Born, 
Annara, 
SweetHome, 
KRD, 
MyfirstLove, 
LoveYourEnemy, 
Svinarnik,
Vetrolom,
VosvrashenieMax,
VtorayShiznZlodeyki,
MirKot,
tridvedma,
charstvoboevixisk,
zlodeykaperevnulac,
kusatludeiinepravilno,
svyatidol,
yastalamateriugg,
TokyoGhoul,
TokyoGhoulRE,
ReinkarVoen,
SaveMe,
NeudPravda, ]

back=InlineKeyboardButton(text="вернуться↩️", callback_data="Back")
clavaTOP.insert(SCB)
clavaTOP.insert(Born)



#clavaTOP.insert(GreenLight)
clavaTOP.insert(btnreturnmenu)

####28


clavaViborGenre=InlineKeyboardMarkup(row_width=1)
buy_pear1 = InlineKeyboardButton(text="Романтика", callback_data="Romantik")
buy_pear2 = InlineKeyboardButton(text="Экшн", callback_data="Ekhn")
buy_pear3 = InlineKeyboardButton(text="Триллер", callback_data="Triller")
buy_pear4 = InlineKeyboardButton(text="Культивация", callback_data="Cultivation")
buy_pear5 = InlineKeyboardButton(text="Драма", callback_data="Drama")
buy_pear6 = InlineKeyboardButton(text="Исекай", callback_data="Isekai")

clavaViborGenre.insert(buy_pear1)
clavaViborGenre.insert(buy_pear2)
clavaViborGenre.insert(buy_pear3)
clavaViborGenre.insert(buy_pear4)
clavaViborGenre.insert(buy_pear5)
clavaViborGenre.insert(buy_pear6)
clavaViborGenre.insert(btnreturnmenu)

ClavaDrama=InlineKeyboardMarkup(row_width=1)
ClavaDrama.insert(TokyoGhoul)
ClavaDrama.insert(TokyoGhoulRE)
ClavaDrama.insert(SaveMe)
ClavaDrama.insert(NeudPravda)
ClavaDrama.insert(Vetrolom)
ClavaDrama.insert(Bastard)
ClavaDrama.insert(SweetHome)
ClavaDrama.insert(back)


Clavaromantik=InlineKeyboardMarkup(row_width=1)
Clavaromantik.insert(buy_pear13)
Clavaromantik.insert(buy_pear14)
Clavaromantik.insert(princ)
Clavaromantik.insert(chertovka)
Clavaromantik.insert(chizel)
Clavaromantik.insert(MyfirstLove)
Clavaromantik.insert(LoveYourEnemy)
Clavaromantik.insert(MirKot)
Clavaromantik.insert(yastalamateriugg)
Clavaromantik.insert(svyatidol)
Clavaromantik.insert(VtorayShiznZlodeyki)
Clavaromantik.insert(zlodeykaperevnulac)
Clavaromantik.insert(tridvedma)
Clavaromantik.insert(back)  #12



ClavaEkhn=InlineKeyboardMarkup(row_width=1)
ClavaEkhn.insert(box)
ClavaEkhn.insert(buy_pear12)
ClavaEkhn.insert(KRD)
ClavaEkhn.insert(Vetrolom)
ClavaEkhn.insert(Born)
ClavaEkhn.insert(kusatludeiinepravilno)
ClavaEkhn.insert(ReinkarVoen)
ClavaEkhn.insert(TokyoGhoul)
ClavaEkhn.insert(TokyoGhoulRE)    #9
ClavaEkhn.insert(back)




clavaTriller=InlineKeyboardMarkup(row_width=1)
clavaTriller.insert(Bastard)
clavaTriller.insert(SweetHome)
clavaTriller.insert(Annara)
clavaTriller.insert(Svinarnik)     #4
clavaTriller.insert(back)


ClavaIsekai=InlineKeyboardMarkup(row_width=1)
ClavaIsekai.insert(charstvoboevixisk)
ClavaIsekai.insert(ReinkarVoen)       #2
ClavaIsekai.insert(VosvrashenieMax)
ClavaIsekai.insert(back)





ClavaCultivation=InlineKeyboardMarkup(row_width=1)
ClavaCultivation.insert(charstvoboevixisk)     #1
ClavaCultivation.insert(btnreturnmenu)




