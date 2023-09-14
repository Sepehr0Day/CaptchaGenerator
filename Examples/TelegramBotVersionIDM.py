from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from CaptchaGenerator.CaptchaGenerator import Captcha

app = Client(
    '',
    api_id=123,  # API ID
    api_hash="",  # API HASH
    bot_token=""  # BOT Token
)

correct_answer = ""
data_user = []

@app.on_message()
async def start(client: Client, message: Message):
    global correct_answer
    keyboard_data = {
        "UpLeft": "↖️",
        "Up": "⬆️",
        "UpRight": "↗️",
        "Left": "⬅️",
        "none": "💠",
        "Right": "➡️",
        "DownLeft": "↙️",
        "Down": "⬇️",
        "DownRight": "↘️",
        "RightCheck": "✓"
    }
    
    keyboard_markup = [
        [
            InlineKeyboardButton(text=keyboard_data[key], callback_data=key)
            for key in row
        ]
        for row in [
            ["UpLeft", "Up", "UpRight"],
            ["Left", "none", "Right"],
            ["DownLeft", "Down", "DownRight"]
        ]
    ]

    Keyboard = InlineKeyboardMarkup(keyboard_markup)

    if message.text == "/start":
        if message.from_user.id in data_user:
            await message.reply_text("Welcome to my bot")
        else:
            address = r"Photos/"
            ImageName, DirArrow = Captcha.CaptchaGeneratorIDR() # You can introduce the photos to 
                                                                # Captcha.CaptchaGeneratorIDR() , 
                                                                # otherwise the program identifies
                                                                # the executable file photos as directional photos.
            correct_answer = DirArrow
            await message.reply_photo(photo=address + ImageName, caption="Select Direction Image", reply_markup=Keyboard)
            pass

@app.on_callback_query()
async def handle_callback(client: Client, callback_query: CallbackQuery):
    global correct_answer, data_user
    directions_texts = ['UpLeft', 'Up', 'UpRight', 'Left', 'Right', 'DownLeft', 'Down', 'DownRight']
    if callback_query.data == correct_answer and correct_answer in directions_texts:
        await callback_query.answer(text=f"Captcha Is True; Welcome {callback_query.message.from_user.first_name}", cache_time=5, show_alert=True)
        data_user.append(callback_query.from_user.id)
        await callback_query.message.delete(revoke=True)
    else:
        await callback_query.answer("Captcha Is Wrong...Try Again")
        await callback_query.message.delete(revoke=True)

app.run()