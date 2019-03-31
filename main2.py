from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize

updater = Updater(token='719614337:AAGVXDHZtOK7YNUsokdtbgjqExNoTEMXxzA')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
  text = update.message.text
  chat_id = update.message.chat_id
  
  if '모해' in text:
    bot.send_message(chat_id=chat_id, text=emojize('광원 오빠 생각:heart_eyes:', use_aliases=True))
  elif '보고 싶어' in text:
    bot.send_message(chat_id=chat_id, text=emojize('나두:heart:', use_aliases=True))
  elif '보구 싶어' in text:
    bot.send_message(chat_id=chat_id, text='나두 보고팡~')
  elif '사진' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/kirara.jpg', 'rb'))
  else:
    bot.send_message(chat_id=chat_id, text='몰라')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)