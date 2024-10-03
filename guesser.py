import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import choice

tocken = '7477297798:AAES0uw09EYEISs0VS5FLnEjtgbiGYbdBsg'
d = {}
bot  = telebot.TeleBot(tocken)

@bot.message_handler(commands = ['start'])
def motivation(msg):
    Oleg = InlineKeyboardMarkup()
    Oleg.add(InlineKeyboardButton('Загадал', callback_data = 'Загадал'))
    bot.send_message(msg.chat.id, 'Загадайте четырёхзначное число из различных цифр', reply_markup = Oleg)
    d[msg.chat.id] = {}
    bot.register_next_step_handler(msg, guess_number)

def gen_number():
    num = choice('123456789')
    num += choice(list(set('0123456789') - set(num)))
    num += choice(list(set('0123456789') - set(num)))
    num += choice(list(set('0123456789') - set(num)))
    return num

def guess_number(call):
    Oleg = InlineKeyboardMarkup()
    Oleg.add(InlineKeyboardButton('0', callback_data = '0 быков'))
    Oleg.add(InlineKeyboardButton('1', callback_data = '1 бык'))
    Oleg.add(InlineKeyboardButton('2', callback_data = '2 быкa'))
    Oleg.add(InlineKeyboardButton('3', callback_data = '3 быкa'))
    Oleg.add(InlineKeyboardButton('4', callback_data = '4 быкa'))
    bot.send_message(call.message.chat.id, f'Я думаю ваше число {gen_number()}')
    bot.send_message(call.message.chat.id, f'Сколько быков?', reply_markup = Oleg)
    

def ask_cows(call):
    Oleg = InlineKeyboardMarkup()
    Oleg.add(InlineKeyboardButton('0', callback_data = '0 коров'))
    Oleg.add(InlineKeyboardButton('1', callback_data = '1 корова'))
    Oleg.add(InlineKeyboardButton('2', callback_data = '2 коровы'))
    Oleg.add(InlineKeyboardButton('3', callback_data = '3 коровы'))
    Oleg.add(InlineKeyboardButton('4', callback_data = '4 коровы'))
    bot.send_message(call.message.chat.id, f'А сколько коров?', reply_markup = Oleg)

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Загадал':
        guess_number(call)
    if call.data[2:5] == 'бык':
        kb = int(call.data[0])
        if kb == 4:
            bot.send_message(call.message.chat.id, f'Победа!')
        else:
            bot.send_message(call.message.chat.id, f'{kb} -- количество быков')
            ask_cows(call)
    if call.data[2:7] == 'коров':
        bot.send_message(call.message.chat.id, f'{call.data[0]} -- количество коров')        
        guess_number(call)

bot.polling()
