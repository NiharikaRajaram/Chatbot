# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:01:03 2018

@author: Rajaram
"""


import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir('C:\\Users\\Rajaram\\Documents\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english\\'):
    data = open('C:\\Users\\Rajaram\\Documents\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english\\' + files, 'r').readline()
    bot.train(data)

while True:
    message = input("You: ")
    if message.strip() == 'bye':
        print("ChatBot: Bye!")
        break
    else:
        reply = bot.get_response(message)
        print("ChatBot: " + str(reply))