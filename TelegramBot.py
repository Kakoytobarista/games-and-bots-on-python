import telebot

bot = telebot.TeleBot('1050444227:AAG-YcWdiPRDS2nWNtwHjBiNPWvxdiUmEdY')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Как дела?', 'Что делаешь?')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'Здравствуй':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как сам?':
        bot.send_message(message.chat.id, 'хорошо, у вас как?')
    elif message.text.lower() == 'что делаешь?' or message.text.lower() == 'чем занят?':
        bot.send_message(message.chat.id, 'переписываюсь с вами')


bot.polling()
