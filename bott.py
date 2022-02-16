import asyncio
import logging
import unittest
import random
from collections import defaultdict
import manhwaclass
import aiogram_broadcaster
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import Message, CallbackQuery
from config import TOKEN, MY_ID, channel_id, QIWI_TOKEN
import keyboardkiwi
import keyboardmainmenu
import keyboardmanhwasetup
from keyboardmainmenu import clava, clavaChangeState, nextchapter, checkSubm, cancelsub, returN
from keyboardkiwi import topup, buy_menu, confirmkb
from keyboardmanhwasetup import clava18,clavaTOP
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from manhwaclass import stateManhwa, is_number
import dictant
from dictant import Herokiller, Maindict, SuicideBoy
import os
from mysql.connector import MySQLConnection
from aiogram_broadcaster import TextBroadcaster
from aiogram_broadcaster import MessageBroadcaster
from aiogram.dispatcher import FSMContext
from db import Database, get
from pyqiwip2p import QiwiP2P
from pathlib import Path

db=Database('testdatabase1.db')
S=stateManhwa()
storage=MemoryStorage()
p2p=QiwiP2P(auth_key=QIWI_TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)
def check_sub_channel(chat_member):
    if chat_member['status']!='left':
        return True
    else:
        return False
#####блок рассылки#####
async def subchanneldone(message: types.Message):
    await bot.send_message('133886300', text="broadcast1337 sheesh")
@dp.message_handler(commands=['sheesh'])
async def subchanneldone(message: types.Message):
    await bot.send_message('133886300', text=get.get_user(1))

@dp.message_handler(commands=['norqo'])
async def subchanneldone(message: types.Message):
    await bot.send_message('133886300', text='/broadcastboxer /broadcastsuicideboy /broadcastsuicideboy /broadcastbastard /broadcastantifanatka /broadcastqueenwithscalpel /broadcastodnazhprinc /broadcastchertovka /broadcast1337 /sheesh /start')
@dp.message_handler(commands=['broadcast1337'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text1')
async def start_broadcast(msg: Message, state: FSMContext):
   
    await state.finish()
    storage = state.storage 
    #users=get.get_user(k)
    await MessageBroadcaster((get.get_user(1)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcast1337')
dp.register_message_handler(start_broadcast, state='broadcast_text1', content_types=types.ContentTypes.ANY)


@dp.message_handler(commands=['broadcastboxer'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text4')
async def start_broadcast(msg: Message, state: FSMContext):
    k=4
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(4)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastboxer')
dp.register_message_handler(start_broadcast, state='broadcast_text4', content_types=types.ContentTypes.ANY)


@dp.message_handler(commands=['broadcastsuicideboy'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text5')
async def start_broadcast(msg: Message, state: FSMContext):
    k=5
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(5)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastsuicideboy')
dp.register_message_handler(start_broadcast, state='broadcast_text5', content_types=types.ContentTypes.ANY)

@dp.message_handler(commands=['broadcastbastard'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text6')
async def start_broadcast(msg: Message, state: FSMContext):
    k=6
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(6)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastbastard')
dp.register_message_handler(start_broadcast, state='broadcast_text6', content_types=types.ContentTypes.ANY)


@dp.message_handler(commands=['broadcastantifanatka'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text7')
async def start_broadcast(msg: Message, state: FSMContext):
    k=4
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(7)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastantifanatka')
dp.register_message_handler(start_broadcast, state='broadcast_text7', content_types=types.ContentTypes.ANY)


@dp.message_handler(commands=['broadcastqueenwithscalpel'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text8')
async def start_broadcast(msg: Message, state: FSMContext):
    k=4
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(8)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastqueenwithscalpel')
dp.register_message_handler(start_broadcast, state='broadcast_text8', content_types=types.ContentTypes.ANY)

@dp.message_handler(commands=['broadcastodnazhprinc'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text9')
async def start_broadcast(msg: Message, state: FSMContext):
    k=4
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(9)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastodnazhprinc')
dp.register_message_handler(start_broadcast, state='broadcast_text9', content_types=types.ContentTypes.ANY)

@dp.message_handler(commands=['broadcastchertovka'])
async def broadcast_command_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для начала рассылки:')
    await state.set_state('broadcast_text10')
async def start_broadcast(msg: Message, state: FSMContext):
    k=4
    await state.finish()
    storage = state.storage 
    users=get.get_user(k)
    await MessageBroadcaster((get.get_user(10)), msg).run()
dp.register_message_handler(broadcast_command_handler, commands='broadcastchertovka')
dp.register_message_handler(start_broadcast, state='broadcast_text10', content_types=types.ContentTypes.ANY)




#####блок рассылки#####

#####блок баланса, пополнения#####
@dp.message_handler(commands=['balance'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"СЧЕТ: {db.user_money(message.from_user.id)} руб.", reply_markup=topup)
@dp.callback_query_handler(text_contains="popolnit")
async def process_video_command(call: CallbackQuery): 
    
    message_money=100
    comment=str(call.message.from_user.id) +"_"+ str(random.randint(1000,9999))
    bill=p2p.bill(amount=message_money, lifetime=15, comment=comment)
    db.add_check(call.message.from_user.id, message_money,bill.bill_id)
    await bot.send_message(call.from_user.id, "пополнение на месячную подписку будет 100 рублей",  reply_markup=buy_menu(url=bill.pay_url, bill=bill.bill_id))
       
@dp.callback_query_handler(text="subscribemanagment")
async def chet(call: CallbackQuery):
    if db.state_subscribe(call.from_user.id)==1:
        await bot.send_message(call.from_user.id, text="у вас уже есть подписка и она дейсвтует до:")
    else:
        await bot.send_message(call.from_user.id, f"сейчас на твоем балансе: {db.user_money(call.from_user.id)} руб.")
        await bot.send_message(call.from_user.id, "подписка дает доступ к самым последним главам таких манхв как:  чтобы ее купить нужно пополнить счет на 100рублей и купить по кнопке :)", reply_markup=topup)
@dp.callback_query_handler(text_contains="check_")
async def process_video_command(call: CallbackQuery):
    bill=str(call.data[6:])
    info=db.get_check(bill)
    print(info)
    if info!=False:
        if str(p2p.check(bill_id=bill).status)== "PAID":
            user_money=db.user_money(call.from_user.id)
            money=int(info[2])
            print(money)
            db.set_money(call.from_user.id, user_money+money)
            await bot.send_message(call.from_user.id, f"ваш счет пополнен на: {money} и теперь он составляет: {user_money}")
        else:
            await bot.send_message(call.from_user.id,text="счет не оплачен чел ало", reply_markup=buy_menu(False,bill=bill))
    else:
        await bot.send_message(call.from_user.id,text="счет не найден")


@dp.callback_query_handler(text="subscribeALL")
async def process_video_command(call: CallbackQuery):
    await bot.send_message(call.from_user.id,text="подписка стоит 100рублей, с баланса спишется 100. Подтверждаем?",reply_markup=confirmkb)

@dp.callback_query_handler(text="confirmpay")   
async def da(message:types.Message):
        if (db.user_money(message.from_user.id)==100 or db.user_money(message.from_user.id)>100):
            newmoney=db.user_money(message.from_user.id)-100
            db.pay_subcribe(message.from_user.id, newmoney)
            subscribe=1
            await bot.send_message(message.from_user.id, text="поздравляю, вы приобрели подписку на месяц")
            print(db.state_subscribe(message.from_user.id))
            db.add_subscribe(message.from_user.id, subscribe)
            print(db.add_subscribe(message.from_user.id, subscribe))
        else:
            await bot.send_message(message.from_user.id, text="мало денег чел", reply_markup=topup)

#####блок баланса, пополнения#####

#####блок старта и основного функционала#####
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    #await bot.send_message('133886300', Herokiller)
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)):
        if not (db.user_exists(message.from_user.id)):
            db.add_user(message.from_user.id)
            await bot.send_message(message.from_user.id, text="привет! сейчас бот работает в тестовом режиме и я буду очень рад, если ты напишешь мне обратную свзяь по работе бота, спасибо! @bububucheel",reply_markup=clava)
        
        else:
            await bot.send_message(message.from_user.id, text="привет! сейчас бот работает в тестовом режиме и я буду очень рад, если ты напишешь мне обратную свзяь по работе бота, спасибо! @bububucheel",reply_markup=clava)
            if not (db.user_exists(message.from_user.id)):
                db.add_user(message.from_user.id)
    else:
         await bot.send_message(message.from_user.id, 'подписка чек', reply_markup=checkSubm)
         if not (db.user_exists(message.from_user.id)):
            db.add_user(message.from_user.id)

@dp.callback_query_handler(text_contains="returnMenu")
async def process_video_command(call: CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer(text="буду рад обратной связи :) @bububucheel",reply_markup=clava)
    buffer=0
    db.addbuffer(call.from_user.id, buffer)
    db.addsearch(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="subscribeNew")    # подписка на выход новых глав чего-либо (реализовать в одном модуле)
async def broad(call:CallbackQuery):
    if db.statebuffer(call.from_user.id)==6:
        if db.state_broadcast_boxer(call.from_user.id)==0:
            boxerbroadcast=call.from_user.id
            db.add_user_broadcast_boxer(call.from_user.id, boxerbroadcast)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?",reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==5:
        if db.state_broadcast_suicideboy(call.from_user.id)==0:
            suicideBoy=call.from_user.id
            db.add_user_broadcast_suicideboy(call.from_user.id, suicideBoy)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?",reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==7:
        if db.state_broadcast_suicideboy(call.from_user.id)==0:
            bastard=call.from_user.id
            db.add_user_broadcast_suicideboy(call.from_user.id, bastard)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?", reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==8:
        if db.state_broadcast_antifanatka(call.from_user.id)==0:
            bastard=call.from_user.id
            db.add_user_broadcast_antifanatka(call.from_user.id, bastard)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?", reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==9:
        if db.state_broadcast_queenwithscalpel(call.from_user.id)==0:
            bastard=call.from_user.id
            db.add_user_broadcast_queenwithscalpel(call.from_user.id, bastard)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?", reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==10:
        if db.state_broadcast_odnazhprinc(call.from_user.id)==0:
            bastard=call.from_user.id
            db.add_user_broadcast_odnazhprinc(call.from_user.id, bastard)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?", reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)
    elif db.statebuffer(call.from_user.id)==11:
        if db.state_broadcast_chertovka(call.from_user.id)==0:
            bastard=call.from_user.id
            db.add_user_broadcast_chertovka(call.from_user.id, bastard)
        else: 
            await call.message.answer("кажется ты уже подписан на выход этой манхвы, хочешь отменить?", reply_markup=cancelsub) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("Мы пришлем тебе новую главу как только она выйдет! :)",reply_markup=cancelsub)






@dp.callback_query_handler(text_contains="cancelmanhwasub")
async def cancelsubfunc(call:CallbackQuery):
    if db.statebuffer(call.from_user.id)==6:
        if db.state_broadcast_boxer(call.from_user.id)==call.from_user.id:
            boxerbroadcast=0
            db.add_user_broadcast_boxer(call.from_user.id, boxerbroadcast)
        else: 
            await call.message.answer("отменили твою подписку!",reply_markup=returN) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("твоя подписка  отменена")
    elif db.statebuffer(call.from_user.id)==5:
        if db.state_broadcast_suicideboy(call.from_user.id)==call.from_user.id:
            suicideBoy=0
            db.add_user_broadcast_suicideboy(call.from_user.id, suicideBoy)
        else: 
            await call.message.answer("отменили твою подписку!",reply_markup=returN) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("твоя подписка отменена")
    elif db.statebuffer(call.from_user.id)==7:
        if db.state_broadcast_suicideboy(call.from_user.id)==call.from_user.id:
            bastard=0
            db.add_user_broadcast_suicideboy(call.from_user.id, bastard)
        else: 
            await call.message.answer("отменили твою подписку!", reply_markup=returN) #в этом блоке нужно дописаь и реализовать функционал отмены рассылки
        await call.message.answer("твоя подписка отменена")



@dp.callback_query_handler(text_contains="саб")
async def subfunc(call:CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await call.message.answer(text="start", reply_markup=clava)
    else:
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)

@dp.callback_query_handler(text_contains="топ")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('🤔 что же выбрать', reply_markup=clavaTOP)

@dp.callback_query_handler(text_contains="18+")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer('рейтинг популярных', reply_markup=clava18)


@dp.callback_query_handler(text_contains="поиск главы")
async def process_video_command(call: CallbackQuery):
    buffer=db.statebuffer(call.from_user.id) 
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer('доступные главы:')
    
    list_keys = list(Maindict[buffer].keys())
    list_keys.sort()
    await bot.send_message(call.from_user.id, text=(list_keys))
   
    await call.message.answer('введи номер главы с которой ты хочешь продолжить читать')
    @dp.message_handler()
    async def buffer(message: types.Message):
            buff=int(message.text)
            db.addsearch(message.from_user.id, buff)
            search=db.statesearch(message.from_user.id)
            buffer=db.statebuffer(message.from_user.id)
            user_id = message.from_user.id
            
            if buff==S.payfullChapters[buffer]:
                   if db.state_subscribe(message.from_user.id)==1:
                        try:
                            await bot.send_message(message.from_user.id, text='глава по подписке')
                            await bot.send_document(message.from_user.id, document=Maindict[buffer][search], reply_markup=nextchapter)
                        except:
                            await bot.send_message(message.from_user.id, text='кажется этой главы еще нет :(', reply_markup=clavaTOP)
                   else:
                        await bot.send_message(message.from_user.id, text='эта глава доступна по подписке')
            else:
                try:
                    await bot.send_document(message.from_user.id, document=Maindict[buffer][search], reply_markup=nextchapter)
                except:
                    await bot.send_message(message.from_user.id, text='кажется этой главы еще нет :(', reply_markup=clavaTOP)






@dp.callback_query_handler(text_contains="начать с начала")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    buffer=db.statebuffer(call.from_user.id)
    await call.message.answer('чтение с нулевой главы')
    await call.bot.send_document(call.from_user.id, document=Maindict[buffer][1], reply_markup=nextchapter)


@dp.callback_query_handler(text_contains="next")
async def nextSERIA(message:types.Message): 
    buffer=db.statebuffer(message.from_user.id)
    search1=db.statesearch(message.from_user.id)+1
    db.addsearch(message.from_user.id, search1)
    search=db.statesearch(message.from_user.id)
    try:
        await bot.send_document(message.from_user.id, Maindict[buffer][search], reply_markup=nextchapter) 
    except:
         await bot.send_message(message.from_user.id, text="кажется эта глава еще не добавлена :(,\n попробуй что нибудь другое", reply_markup=clavaTOP)

'''
@dp.callback_query_handler(text_contains="download")
async def process_video_command(call: CallbackQuery):
    buffer=db.statebuffer(call.from_user.id)
    for i in range(0,)
    await bot.send_document(call.from_user.id, Maindict[buffer][i]
'''
#####блок старта и основного функционала#####




#####блок callbackov манхв#####

@dp.callback_query_handler(text_contains="Eliced")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nКайден - загадочный человек, который словно комета спустился с неба. Весь израненный, почти потерявший последние силы, он решает скрыть свое присутствие - ведь по-другому от погони не уйти. По дороге Кайден встречает обычную дворовую кошку и, почти не думая, решает вселиться в ее тело. Со Джи У - энергичный и общительный молодой человек из средней школы, который...\n*Оценка на мангалибе: 4.94*', photo='AgACAgIAAxkDAAIL5WIKCLEcLgoWAYWrvmFjNdXQ62f7AALFtTEb2xlRSB5WFiNG9AjqAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('Кайден - загадочный человек, который словно комета спустился с неба. Весь израненный, почти потерявший последние силы, он решает скрыть свое присутствие - ведь по-другому от погони не уйти. По дороге Кайден встречает обычную дворовую кошку и, почти не думая, решает вселиться в ее тело. Со Джи У - энергичный и общительный молодой человек из средней школы, который ', reply_markup=clavaChangeState)
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=4
    db.addbuffer(call.from_user.id, buffer)
 



@dp.callback_query_handler(text_contains="SuicideBoy")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nОСТОРОЖНО! Эта манхва может содержать неприятные сцены для просмотра. Не рекомендуется к просмотру несовершеннолетним и слабонервным людям с неустойчивой психикой. Семнадцатилетний школьник Ли Хун - подросток, то вконец разочаровывающийся в жизни, то снова обретающий надежду, находя новых друзей. Его жизнь больше походит на тяжёлую драму с нотками комедии. В худшие периоды своей жизни погружается в нерадужные мысли о своём исчезновении, но даже несмотря на это продолжает жить... Манхва предоставляет нам психологический портрет подростка с депрессией, позволяет следить за эмоциональными скачками героя, за раскрытием его личности.\n*Оценка на мангалибе: 4.88*', photo='AgACAgIAAxkDAAIL32IKCK78b0w6W4wObZ0InSJ4B9e_AALAtTEb2xlRSJHaJhoLFlk0AQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('ОСТОРОЖНО! Эта манхва может содержать неприятные сцены для просмотра. Не рекомендуется к просмотру несовершеннолетним и слабонервным людям с неустойчивой психикой. Семнадцатилетний школьник Ли Хун - подросток, то вконец разочаровывающийся в жизни, то снова обретающий надежду, находя новых друзей. Его жизнь больше походит на тяжёлую драму с нотками комедии. В худшие периоды своей жизни погружается в нерадужные мысли о своём исчезновении, но даже несмотря на это продолжает жить... Манхва предоставляет нам психологический портрет подростка с депрессией, позволяет следить за эмоциональными скачками героя, за раскрытием его личности. оценка на мангалибе: 4.8', reply_markup=clavaChangeState)
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=5
    db.addbuffer(call.from_user.id, buffer)


@dp.callback_query_handler(text_contains="Boxer")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nШокирующий талант, с которым никто не может столкнуться! Это благословение или проклятие?! \n*Оценка на мангалибе: 4.88*', photo='AgACAgIAAxkDAAIL4WIKCK83_zqk5jeHSSqJk4Z2Kl1PAALBtTEb2xlRSA6GyX-DFqhKAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('Шокирующий талант, с которым никто не может столкнуться! Это благословение или проклятие?! оценка на реманге: 9.4', reply_markup=clavaChangeState)
        

    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=6
    db.addbuffer(call.from_user.id, buffer)
    #db.statebuffer(call.from_user.id)
#########сделать
@dp.callback_query_handler(text_contains="Bastard")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nДжин Сон нигде не может найти утешения. В школе над ним безжалостно издеваются из-за его замкнутого характера и слабого здоровья. Однако не это является источником непреодолимого ужаса Джина: то, что он боится больше всего, — это его собственный отец. Для большинства отец Джина — отзывчивый человек, успешный бизнесмен и любящий родитель. Но это только видимость.\n*Оценка на мангалибе: 4.9*', photo='AgACAgIAAxkDAAIL4mIKCLC-SvMBGl0V-UIYFhKsETAYAALCtTEb2xlRSI96MNJPRWRBAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('Джин Сон нигде не может найти утешения. В школе над ним безжалостно издеваются из-за его замкнутого характера и слабого здоровья. Однако не это является источником непреодолимого ужаса Джина: то, что он боится больше всего, — это его собственный отец. Для большинства отец Джина — отзывчивый человек, успешный бизнесмен и любящий родитель. Но это только видимость. Оценка на мангалибе: 4.9', reply_markup=clavaChangeState)
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=7
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="antifanatka")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nКаково жить с собственным хейтером? Популярный айдол Ху Джун почувствовал это на собственном опыте, вынужденно поселившись вместе со своей анти-фанаткой – репортером Ли Гын Ён. Что принесёт этим двоим такое сожительство? Изведут они друг друга или между ними зародится нечто новое?.. \n*Оценка на мангалибе: 4.75*', photo='AgACAgIAAxkDAAIL5GIKCLGnuj371btPFVxVWUpMhXxRAALEtTEb2xlRSFcIIIdzac2rAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('Каково жить с собственным хейтером? Популярный айдол Ху Джун почувствовал это на собственном опыте, вынужденно поселившись вместе со своей анти-фанаткой – репортером Ли Гын Ён. Что принесёт этим двоим такое сожительство? Изведут они друг друга или между ними зародится нечто новое?.. ', reply_markup=clavaChangeState)
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=8
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="queenwithscalpel")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nВ первой жизни она была ужасной королевой, навлёкшей на страну беды и сожжённой своим же королём на костре. Во второй - стала талантливым хирургом, искупающим свою вину за прошлое, спасая людей. Но из-за авиакатастрофы талантливый хирург Сон Чжи Хён вернулась в свою первую жизнь! В этот раз она решила всё изменить, став врачом.\n*Оценка на мангалибе: 4.73*', photo='AgACAgIAAxkDAAIL3mIKCK4kL9PFamo1U5ydTpjbsNRRAAK_tTEb2xlRSEcLI1AWgTWqAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('В первой жизни она была ужасной королевой, навлёкшей на страну беды и сожжённой своим же королём на костре. Во второй - стала талантливым хирургом, искупающим свою вину за прошлое, спасая людей. Но из-за авиакатастрофы талантливый хирург Сон Чжи Хён вернулась в свою первую жизнь! В этот раз она решила всё изменить, став врачом. Оценка на мангалибе:4.73', reply_markup=clavaChangeState)
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=9
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="odnazhprinc")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \n Когда я открыла глаза, то стала принцессой из романа, который я читала. Но почему из всех персонажей этой истории именно принцессой, судьба которой тесно переплетена с кровавым Императором? Если я хочу выжить, то должна быть неприметной для его глаз и сбежать! «Когда это в моём дворце начали жить ничтожные людишки?».\n*Оценка на мангалибе: 4.93*', photo='AgACAgIAAxkDAAIL42IKCLA8g1KSatm0XYoP_wMBrZxAAALDtTEb2xlRSBJIkDxmd9TQAQADAgADeAADIwQ', reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer('Когда я открыла глаза, то стала принцессой из романа, который я читала. Но почему из всех персонажей этой истории именно принцессой, судьба которой тесно переплетена с кровавым Императором? Если я хочу выжить, то должна быть неприметной для его глаз и сбежать! «Когда это в моём дворце начали жить ничтожные людишки?». Оценка на мангалибе: 4.93', reply_markup=clavaChangeState)
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=10
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="chertovka")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \n Я стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*Оценка на мангалибе: 4.83*', photo="AgACAgIAAxkDAAIL2GIKB1GDpvSeqU4vWnm7LF4lorZRAAK7tTEb2xlRSGmFT2oZ-TqcAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=11
    db.addbuffer(call.from_user.id, buffer)



@dp.callback_query_handler(text_contains="chizel")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nСловно мятежный дух, пойманный в ловушку, Жизель находясь в браке с жестоким мужем, ведёт жалкую жизнь, играя роль кроткой жены и леди. Но однажды ночью, блуждая по своему новому дому, Жизель обнаруживает маленького мальчика, запертого в клетке. Похоже, что он — это наследство от эксцентричного отца её мужа. Мальчика считают монстром, «бессмертным цветком, питающимся кровью». Несмотря на свой страх, Жизель начинает навещать мальчика по ночам. Разрушат ли эти незаконные встречи её жизнь?♡ \n*Оценка на мангалибе: 4.9*', photo="AgACAgIAAxkDAAIMd2IKIgyXR5jWEYteFAfLRj86uLNFAAI7tjEb2xlRSOxINr4IXP-rAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=12
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="Born")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nЮй Идзинь когда-то был единственным выжившим в авиакатастрофе. Чтобы выжить, он становится наёмником. Спустя 10 лет он возвращается к своей семье в родной город. Сможет ли он забыть свое прошлое и жить жизнью обычного школьника? \n*Оценка на мангалибе: 4.91*', photo="AgACAgIAAxkDAAIMeWIKIpYNyHa7hMsB9IlNrOejbl4dAAJCtjEb2xlRSLiyF7UGtd6PAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=13
    db.addbuffer(call.from_user.id, buffer)
    

@dp.callback_query_handler(text_contains="Annara")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nВ школе ходит слух о том, что в заброшенном парке развлечений живёт фокусник, который на самом деле является магом и может взаправду разрезать человека пополам, а потом соединить обратно. А когда он показывает номер с исчезновением, то человек исчезает на самом деле.\n*Оценка на мангалибе: 4.85*', photo="AgACAgIAAxkDAAIchGIM3x_9Qvt20VxrVLdSKfOLBrcAAxm7MRuRIGhIqB31IUmUFYUBAAMCAAN4AAMjBA", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=14
    db.addbuffer(call.from_user.id, buffer)


@dp.callback_query_handler(text_contains="SweetHome")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nТвоя задротская душа Не любит всех — только себя.Ты шлёшь семью и мир вокруг, И без друзей твой ближний круг. Но как бывает иногда, Лишь потеряв всё навсегда, Решил ты небо не коптить И суицид взять совершить. Но мир на блажь твою плевал И кучу ужасов наслал. Теперь придётся как-то жить... Ну и всех монстров победить? (с) RSC \n*Оценка на мангалибе: 4.9*', photo="AgACAgIAAxkDAAIcj2IM4M-FrGj2uHqPDuwIDG_hh3K2AAIeuzEbkSBoSBQTVaf0l0GjAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=15
    db.addbuffer(call.from_user.id, buffer)


@dp.callback_query_handler(text_contains="KRD")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nСо 140-ой главы начала выходить цветная электронная версия манги.Танджиро - старший сын в семье, потерявшей кормильца. Однажды он уходит в другой город, чтобы продать древесный уголь, но в конце концов остаётся на ночь в чужом доме, вместо того, чтобы идти домой. А всё из-за слухов о демоне, который разгуливает в горах под покровом темноты. Утром парень вернётся домой живым и невредимым... Но его ждут ужасные известия.\n*Оценка на мангалибе: 4.88*\n *Цветная версия только со 140 главы, жмите сразу "я знаю с какой главы начать читать"*', photo="AgACAgIAAxkDAAIhVWINR-aKU3-Tz-yo8dyvgNeYy1u9AAJVvDEbkSBoSNxtsPC6YGn7AQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=16
    db.addbuffer(call.from_user.id, buffer)



@dp.callback_query_handler(text_contains="MyfirstLove")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nХуа Цяньшу — старшеклассница, которая благодаря отцу поступила в престижную школу-интернат. Здесь дети из небогатых семей ведут себя довольно скромно, чтобы не стать объектом насмешек. Но девушка больше не в силах терпеть школьного хулигана, поэтому решается на отважный шаг — записать на видео его издевательства над одноклассником. Кто же знал, что данное действие навсегда изменит ее мирную школьную жизнь…\n*Оценка на мангалибе: 3.94 sad :(*', photo="AgACAgIAAxkDAAIhVmINR-i4JuEPuHq9EhfREbJl9djtAAJWvDEbkSBoSIz6ui4JhNfpAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=17
    db.addbuffer(call.from_user.id, buffer)


@dp.callback_query_handler(text_contains="LoveYourEnemy")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \nНаучившись искусно лгать на протяжении всей своей жизни, Пэ Ён Хи поклялась оставить своё прошлое позади и начать новую жизнь, поступив в университет в 24 года. Но, когда она сталкивается с тем, кто знает её секрет из прошлого, который может полностью разрушить её репутацию, то её надежды на идеальную жизнь начинают рушиться. Среди студенческих сплетен, влюблённостей и ревности, могут ли эти двое отбросить свои разногласия и принять друг друга такими, какие они есть на самом деле?\n*Оценка на мангалибе: 4.81*', photo="AgACAgIAAxkDAAIhVGINR-YF95Xh26SBCtAzU4asnp7PAAJUvDEbkSBoSOP8cfM3sruqAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=18
    db.addbuffer(call.from_user.id, buffer)

@dp.callback_query_handler(text_contains="GreenLight")
async def process_video_command(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, caption='*Описание:* \n«…Я хочу воплотить ваш образ в скульптуре. В форме, что навеки останется неизменной". В городе, полном высотных зданий, Мэттью Рейнор, студент-скульптор, живет жизнью одиночки, изолировавшись от остального мира. Неожиданно он встречает на своем пути прекрасного мужчину по имени Цзинь Цинь-Ю и чувствует, что эта встреча была дарована ему самой судьбой. Мэттью делает мужчине предложение: стать моделью для его скульптуры. \n*Оценка на мангалибе: 4.94*\n яой', photo="AgACAgIAAxkDAAIhl2INS1FiHjXA86rCddRyF-y4kbNcAAJgvDEbkSBoSF7EynoeiL5yAQADAgADeAADIwQ", reply_markup=clavaChangeState, parse_mode="Markdown")
        #await call.message.answer(text='*Описание:* \nЯ стала злодейкой любовного романа. Думаете, меня что-то не устраивает? Нет, всё просто прекрасно. Статус дочери герцога даёт возможность жить в роскоши и комфорте, и я собираюсь извлечь всю выгоду из своего нынешнего положения. Но, хотя я не хочу идти по пути антагонистки, белой и пушистой тоже не буду. Мой жених изменил мне с главной героиней, поэтому я перепишу оригинальную историю и поставлю всех на колени. Эти ублюдки не стоят моих слёз. \n*оценка на мангалибе: 4.83*', reply_markup=clavaChangeState, parse_mode="Markdown")
        
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.bot.send_message(call.from_user.id, 'Для просмотра сначала подпишись на канал', reply_markup=checkSubm)
    buffer=19
    db.addbuffer(call.from_user.id, buffer)



#####блок callbackov манхв конец#####





























































if __name__ == '__main__':
    executor.start_polling(dp)






