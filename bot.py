# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
import json
from key_generation import generate_key
# from read_write import readData, writeDate



def SendToGeneratePage(payload):
    url = "http://194.67.91.175/api/v1/generatepage/"
    headers = {
    'Content-Type': 'application/json'
    }
    print(json.dumps(payload))
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))
    return(json.loads(response.text.encode('utf8')))


dannnye = {
    "0id": {
	"name":"",
	"foto":"",
	"date_1":"",
	"date_2":"12 июня 1944",
	"description":"Вся наша семья гордится Дедом. Спасибо Ветераны за Победу!",
	"city":"",
	"units":"130 сп",
    "url":""
}}

bot = telebot.TeleBot('1285880883:AAGV3yp19a1u8jud_kAUrhFTEhsltSmN8Fk')
markup = types.ReplyKeyboardRemove(selective=False) 
@bot.message_handler(commands=['menu'])
def load_menu(message, text):
    markup_menu = types.ReplyKeyboardMarkup(row_width=4)
    itembtn1 = types.KeyboardButton('Этап 1. Ввести ФИО')
    itembtn2 = types.KeyboardButton('Этап 2. Добавить фотографию')
    itembtn3 = types.KeyboardButton('Этап 3. Ввести дату рождения')
    itembtn4 = types.KeyboardButton('Этап 4. Выбрать город призыва')
    markup_menu.add(itembtn1, itembtn2, itembtn3, itembtn4)
    url_button = types.InlineKeyboardButton(text="Сформировать отчет", url="https://ya.ru")
    markup_menu.add(url_button)
    bot.send_message(message.chat.id, text, reply_markup=markup_menu) 

@bot.message_handler(commands=['menu_photo'])
def load_menu_photo(message, text):
    markup_menu = types.ReplyKeyboardMarkup(row_width=1)
    itembtn2 = types.KeyboardButton('Этап 2. Добавить фотографию')
    markup_menu.add(itembtn2)
    bot.send_message(message.chat.id, text, reply_markup=markup_menu) 

@bot.message_handler(commands=['menu_data'])
def load_data(message, text):
    markup_menu = types.ReplyKeyboardMarkup(row_width=1)
    itembtn3 = types.KeyboardButton('Этап 3. Ввести дату рождения')
    markup_menu.add(itembtn3)
    bot.send_message(message.chat.id, text, reply_markup=markup_menu)

@bot.message_handler(commands=['menu_city'])
def load_city(message, text):
    markup_menu = types.ReplyKeyboardMarkup(row_width=1)
    itembtn4 = types.KeyboardButton('Этап 4. Ввести город призыва')
    markup_menu.add(itembtn4)
    bot.send_message(message.chat.id, text, reply_markup=markup_menu) 
@bot.message_handler(commands=['report'])
def load_report(message, text):
    markup_menu = types.ReplyKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Получить отчет", url="https://ya.ru")
    markup_menu.add(url_button)
    bot.send_message(message.chat.id, text, reply_markup=markup_menu)     
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Добрый день, я Ваш помощник в поиске информации о Вашем Герое!", reply_markup=markup)  
    load_menu(message, text="К сожалению, мне нужно немного помочь... Выберете пункт меню")

####ФИО
def fio_search(message):
    teamname=message.text
    try:
        ans="Получено: " + teamname#"Это имя
        dannnye.update({message.chat.id:{"name":teamname,"units":"130 сп","description":"Вся наша семья гордится Дедом. Спасибо Ветераны за Победу!"}})
        load_menu_photo(message, text = ans)
    except Exception as e:
        bot.send_message(message.chat.id,e, reply_markup=markup)
        
@bot.message_handler(func=lambda m: m.text is not None and 'Этап 1' in m.text)
def echo2(message):   
    msg = bot.reply_to(message,"Введите в текстовом поле данные")
    bot.register_next_step_handler(msg, fio_search)



####ФОТО
@bot.message_handler(func=lambda m: m.text is not None and 'Этап 2' in m.text)
def echo3(message):   
    msg = bot.reply_to(message,"Загрузите фото Героя") 

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    ans = 'Изображение загружено'#Адрес соообщения; ' + message.photo[0].file_id #Это id foto https://api.telegram.org/bot1285880883:AAGV3yp19a1u8jud_kAUrhFTEhsltSmN8Fk/getFile?file_id=ID
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    key = generate_key()
    with open(f"{key}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    dannnye[message.chat.id].update({"foto":f"{key}.jpg"})
    msg = bot.reply_to(message, ans)
    #msg =  bot.reply_to(message,"Получено")
    load_data(message, text = 'Спасибо! Введите дату или год рождения.')
    bot.register_next_step_handler(msg, data_raw)

####Дата
@bot.message_handler(func=lambda m: m.text is not None and 'Этап 3' in m.text)
def echo4(message):   
    msg = bot.reply_to(message,"Введите дату рождения")

def data_raw(message):
    ans="Введите город призыва"
    #load_city(message, text = ans)
    city = 'Дата: ' + message.text #Это дата
    dannnye[message.chat.id].update({"date_1":message.text})
    bot.send_message(message.chat.id,city, reply_markup=markup)
    load_city(message, text = 'Спасибо! Введите город призыва.')
    bot.register_next_step_handler(message, city_raw)
    
####Город
@bot.message_handler(func=lambda m: m.text is not None and 'Этап 4' in m.text)
def echo5(message):   
    msg = bot.reply_to(message,"Введите город призыва")
def city_raw(message):
    city = 'Город: ' + message.text#Это город
    dannnye[message.chat.id].update({"city":message.text})
    bot.send_message(message.chat.id,city, reply_markup=markup)
    urll = SendToGeneratePage(dannnye[message.chat.id])['url']
    dannnye[message.chat.id].update({"url":urll})
    load_report(message, text = 'Спасибо! Получите ссылку на отчет.')
    
###Отчет
@bot.message_handler(func=lambda m: m.text is not None and 'Получить отчет' in m.text)
def photo_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажмите на меня", url=dannnye[message.chat.id]['url'])#поставить адрес
    keyboard.add(switch_button)
    bot.send_message(message.chat.id, "Спасибо, что гордитесь Героями!", reply_markup=keyboard)
   
bot.polling()