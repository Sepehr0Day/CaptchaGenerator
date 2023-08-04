from pyrogram import Client
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from CaptchaGenerator.CaptchaGenerator import CaptchaGeneratRandom
import pyromod

app = Client(
    'app', 
    api_id=123, # API ID
    api_hash="", # API HASH
    bot_token="" # BOT Token
)

correct_answer = ""
data_user = []

@app.on_message()
async def start(client: Client, message: Message):
    global correct_answer
    if message.text == "/start":
        if message.from_user.id in data_user:
            await message.reply_text("Welcome to my bot")
        else:
            correct_answer, variants = CaptchaGeneratRandom(NumberGen=5 , ValuesCaptcha="0123456789abc" , NumberVariants=6 , Backgrounds=["Background\Background1.png" , "Background\Background2.png"] , Fonts=["fonts\BrunoAce-Regular.ttf" , "fonts\AmaticSC-Bold.ttf"]  , NameExport="CaptchaGeneratorRandom" , PathExport=r"c:\Users\sepeh\Desktop\Successful projects\Captcha Generator") 
            print(correct_answer)
            keyboard_buttonsin = [
               [InlineKeyboardButton(variant, callback_data=variant) for variant in row]
              for row in [variants[i:i + 2] for i in range(0, len(variants), 2)]
            ]
            keyboard_markupin = InlineKeyboardMarkup(keyboard_buttonsin)
            message = await message.reply_photo(photo=r"c:\Path\CaptchaGeneratorRandom.png" , reply_markup=keyboard_markupin)

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