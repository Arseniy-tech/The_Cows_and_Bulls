import telebot
from random import choice


tocken = '7477297798:AAES0uw09EYEISs0VS5FLnEjtgbiGYbdBsg'
d = {}
bot  = telebot.TeleBot(tocken)


@bot.message_handler(commands = ['start'])
def motivation(homyak_topping):
    if homyak_topping.chat.id not in d:
        bot.send_message(homyak_topping.chat.id, 'Я загадал число.')
        d[homyak_topping.chat.id] = choice('123456789')
        d[homyak_topping.chat.id] += choice(list(set('0123456789') - set(d[homyak_topping.chat.id])))
        d[homyak_topping.chat.id] += choice(list(set('0123456789') - set(d[homyak_topping.chat.id])))
        d[homyak_topping.chat.id] += choice(list(set('0123456789') - set(d[homyak_topping.chat.id])))
        # bot.send_message(homyak_topping.chat.id, f'ЧИТКОД: {d[homyak_topping.chat.id]}')
    else:
        bot.send_message(homyak_topping.chat.id, 'Пиши число.')

@bot.message_handler(content_types=['text'])
def text_handler(msg):
    if msg.chat.id not in d:
        bot.send_message(msg.chat.id, 'Для старта используйте команду /start')
    elif not msg.text.isdigit():
        bot.send_message(msg.chat.id, 'Можно вводить только цифры')
    elif len(msg.text) != 4:
        bot.send_message(msg.chat.id, 'Можно вводить только 4 цифры')
    elif msg.text[0] == '0':
        bot.send_message(msg.chat.id, 'Нельзя начинать с нуля')
    elif len(set(msg.text)) != 4:
        bot.send_message(msg.chat.id, 'Нужно ввести 4 разных цифры')
    else:
        bulls = 0
        for i in range(4):
            if d[msg.chat.id][i] == msg.text[i]:
                bulls += 1
        cows = len(set(d[msg.chat.id]) & set(msg.text)) - bulls
        bot.send_message(msg.chat.id, f'коров = {cows}, быков = {bulls}')
        if bulls == 4:
            bot.send_message(msg.chat.id, 'Молодец, ты уничтожил галактику!')
            del d[msg.chat.id]


bot.polling()
