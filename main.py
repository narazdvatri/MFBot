import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
links = []
list = []
with open('list.txt', 'r') as f:
    list = f.readlines()

with open('links.txt', 'r') as f:
    links = f.readlines()


def start(bot,update):

    update.message.reply_text('@MinterFAQBot – бот с которым Вы за считанные\n'
                              'секунды найдете ссылку с ответом на вопрос о\n'
                              'блокчейн-проекте Minter.Network.')

    # bot.send_video(chat_id=update.message.chat_id, video=open('video.mp4', 'rb'), supports_streaming=True)



import time
def inlinequery(update, context):
    query = update.inline_query.query
    number = []
    a = [number.append(i) for i in range(len(list)) if query in list[i]]
    results = []

    if len(number)!=0:

        for i in range(len(number)):
            results.append(InlineQueryResultArticle(
                id=uuid4(),
                title=list[number[i]],
                thumb_width =30,
                thumb_height =12,
                input_message_content=InputTextMessageContent(
                    links[number[i]])))
    else:
        for i in range(5):
            results.append(InlineQueryResultArticle(
                id=uuid4(),
                title=list[i+68],
                thumb_width=30,
                thumb_height=12,
                input_message_content=InputTextMessageContent(
                    links[i+68])))

    update.inline_query.answer(results)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("926861603:AAEEwvfQL6xBCG6SaaU9Wd5EQfEKPGsQxeI",use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
