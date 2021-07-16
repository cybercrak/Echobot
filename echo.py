import os 
import telebot

KEY = "1763777622:AAEwCO4LU1rPUlfGf1Bc-BBCJucrAYPyMaw"

bot=telebot.TeleBot(KEY)

@bot.message_handler(commands=["start"])
def send(message):
	bot.reply_to(message,"Hello welcome to EchoBot 😁\n\nI will just echo for all your messages have fun😝")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message,message.text)

bot.polling()
