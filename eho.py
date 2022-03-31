import telebot


bot = telebot.TeleBot("5143965673:AAFmsqtlpibTzMl6K_bs0VT_4lFfrcH4mQo")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
