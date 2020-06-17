import telebot
import telegram
bot = telebot.TeleBot('1181885362:AAE-miH7zobHB1qQ-nqzoiNY82RkRGPCPTQ')

@bot.message_handler(commands=['start'])
def start(message):
    who = message.chat.id
    bot.send_message(who,"Текст")


@bot.message_handler(content_types=['text'])
def send_mes(message):
    who = message.chat.id
    bot.send_message(who, "Текст")
    bot.send_message(who, "Текст")
    bot.send_message(chat_id=who,
                     text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.',
                     parse_mode=telegram.ParseMode.HTML)
    bot.send_message(chat_id=who,
                     text='<u>QWDNkjdnыламтавл124</u> ',
                     parse_mode=telegram.ParseMode.HTML)
    bot.send_message(chat_id=who,
                     text='<s>QWDNkjdnыламтавл124</s> ',
                     parse_mode=telegram.ParseMode.HTML)
    bot.send_message(chat_id=who,
                     text='<code>QWDNkjdnыламтавл124</code> ',
                     parse_mode=telegram.ParseMode.HTML)
    bot.send_message(chat_id=who,
                     text='<pre>QWDNkjdnыламтавл124</pre> ',
                     parse_mode=telegram.ParseMode.HTML)
    bot.send_message(chat_id=who,
                     text='<b>bold <i>italic</i></b> ',
                     parse_mode=telegram.ParseMode.HTML)

print('go')
bot.polling(none_stop=True)