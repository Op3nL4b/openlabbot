#Per avviare il bot, digitare python main.py da terminale
import sys
import time
import telepot
from customKeyboard import *

print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)