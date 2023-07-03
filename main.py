import os
import telebot


bot = telebot.TeleBot("2111353168:AAGMUnFi8LM_ObHGK21oc8rUfNZXXevXI-c")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm test Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/SlNinjaTeam")



bot.polling()
