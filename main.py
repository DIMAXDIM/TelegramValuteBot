import telebot
from extencions import *
from config import *

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'to start work,write any currency what you want to trade,then currency what you want to claim,at the end write amount\nneed to look like that\n"dollar ruble 12"'
    bot.reply_to(message, text)
@bot.message_handler (commands=['values'])
def values (message: telebot.types.Message):
    text = 'currency which you can trade'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)
                 

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3 :
            raise ConvertException('you need to send message in this format\ndollar ruble 1')
        quote, base, amount = values
        total_base = ValuteConvertor.convert(quote, base, amount)
    except ConvertException as e:
        bot.reply_to(message, f'user error \n{e}')
    except Exception as e:
        bot.reply_to(message, f'failed the procces, i dont know command\n{e}')

    else:
        text = f'{amount} {quote}s   ---->   in {base}s is {total_base * float(int(amount))}'
        bot.send_message(message.chat.id, text)
        






















bot.polling(none_stop=True)























