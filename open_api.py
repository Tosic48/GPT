# Что такое Chat GPT - создаем Телеграм бот для общения с нейросетью OpenAI

# Подписывайтесь, чтобы
# быстрее узнавать о
# новых уроках - https://t.me/isartem_bot

# pip install pyTelegramBotAPI
# pip install openai
from config import api_ident
import telebot
import openai


bot = telebot.TeleBot("6023813534:AAE6i3zDhxSX_ZGs74dbQlMSqmpfAjLWmw0")
openai.api_key = api_ident

@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()