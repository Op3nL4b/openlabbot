# -*- coding: utf-8 -*-
import sys
import time
import telepot
import datetime
import webbrowser
from parserHTML import *
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

url = "http://openlab.dibris.unige.it/index.php/lego"

def createLog(msg):
    datemsg = datetime.datetime.fromtimestamp(
            int(msg['date'])
            ).strftime('%Y-%m')
    monthLog = datetime.datetime.now().strftime('%Y-%m')
    report = datetime.datetime.fromtimestamp(
            int(msg['date'])
            ).strftime('%Y-%m-%d %H:%M:%S'),msg['message_id'],msg['from'],msg['text']
    report = str(report)
    if monthLog!=datemsg:
        monthLog = datemsg
    out_file = open( "logs/" + monthLog + ".txt" ,"a")
    out_file.write(report + "\n")
    out_file.close()

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    createLog(msg)
    if content_type == 'text':
        if (msg['text'] == '/help' or msg['text'] == '/start'):
            bot.sendMessage(chat_id, 'Come posso aiutarti?',
                            reply_markup=ReplyKeyboardMarkup(
                                resize_keyboard = True,
                                keyboard=[
                                    [KeyboardButton(text="Orari"), KeyboardButton(text="Eventi"),KeyboardButton(text="Progetti attivi"),KeyboardButton(text="Chi siamo")]
                                ]
                            ))
        elif msg['text'] == 'Orari':
            bot.sendMessage(chat_id,'https://docs.google.com/spreadsheets/d/1Ce80qmF-nKEcuUJmqiLCYEUBZtCyQmVH-x_M-ZwnCKY/pubhtml/sheet?headers=false&gid=1104399453')
        elif msg['text'] == 'Eventi':
            bot.sendMessage(chat_id,'Work in progress')
        elif msg['text'] == 'Progetti attivi':
            bot.sendMessage(chat_id,funcParserHTML(url))
        elif msg['text'] == 'Chi siamo':
            bot.sendMessage(chat_id,'L\'0p3n_L4b è un laboratorio interamente gestito da studenti il cui scopo è fornire ulteriori competenze ed, eventuale supporto agli studenti del Dipartimento DIBRIS sviluppando progetti.\n\nopenlab.dibris.unige.it')
    elif content_type == 'photo':
        bot.sendMessage(chat_id,'Mi hai inviato una foto, ancora non posso leggerla')

bot = telepot.Bot('TOKEN INSERT')


