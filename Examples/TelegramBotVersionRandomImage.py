import os
import random
import requests
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from CaptchaGenerator.CaptchaGenerator import Captcha

app = Client(
    'app',
    api_id=123,  # API ID
    api_hash="",  # API HASH
    bot_token=""  # BOT Token
)

correct_answer = ""
data_user = []

def translate_text(text, target_lang):
    url = "https://translate.google.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en", 
        "tl": target_lang,
        "dt": "t",
        "q": text
    }
    response = requests.get(url, params=params)
    data = response.json()
    translated_text = data[0][0][0]
    return translated_text

@app.on_message()
async def start(client: Client, message: Message):
    global correct_answer
    if message.text == "/start":
        if message.from_user.id in data_user:
            await message.reply_text("Welcome to my bot")
        else:
            folder_path = r"C:\Path\Photos"
            ImageSelected, ImageSelectedName, ImageSelectedFormat, ImageNamesInFolder = Captcha.CaptchaGeneratorImageRandom(folder_path , 7)
            Targetlanguage = "fa" #You Can Set Your Language For Translate
            translated_names = [f"{name} | {translate_text(name, Targetlanguage).strip()}"
                                for name in ImageNamesInFolder]
            correct_answer = ImageSelectedName
            randomized_indices = list(range(len(translated_names)))
            random.shuffle(randomized_indices)
            
            keyboard_buttonsin = [
                [InlineKeyboardButton(translated_names[i], callback_data=ImageNamesInFolder[i])]
                for i in randomized_indices
            ]
            keyboard_markupin = InlineKeyboardMarkup(keyboard_buttonsin)
            await message.reply_photo(photo=folder_path + r"\\" + ImageSelected, reply_markup=keyboard_markupin)

@app.on_callback_query()
async def handle_callback(client: Client, callback_query: CallbackQuery):
    if callback_query.data == correct_answer:
        await callback_query.answer("Captcha is True", show_alert=True, cache_time=8)
        await callback_query.message.delete(revoke=True)
        data_user.append(callback_query.from_user.id)
        await callback_query.message.reply_text("Welcome to my bot")
    else:
        await callback_query.answer("ERROR!", show_alert=True, cache_time=8)
        await callback_query.message.delete(revoke=True)

app.run()
