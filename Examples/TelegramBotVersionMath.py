import pyromod
from pyrogram import Client
from pyrogram.types import Message
from CaptchaGenerator.CaptchaGenerator import Captcha

app = Client(
    '',
    api_id=123,  # API ID
    api_hash="",  # API HASH
    bot_token=""  # BOT Token
)

data_user = []
@app.on_message()
async def start(client: Client, message: Message):
    
    if message.text == "/start":
        if message.from_user.id in data_user:
            await message.reply_text("Welcome to my bot")
        else:
            CaptchaEquation , CaptchaCorrect = Captcha.CaptchaGeneratorMath()            
            CaptchaMath = await message.reply_text(f"Solve The Equation : {CaptchaEquation} ")
            GetSolve = await message.chat.ask("Solve Insert The Equation : ")
            if int(GetSolve.text) == CaptchaCorrect:
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaMath.id , GetSolve.id , message.id] , revoke=True)
                await message.reply_text("Captcha is True\nWelcome To My Bot!")
                data_user.append(message.from_user.id)
            else:
                await message.reply_text("Captcha is Wrong!!\n/start")
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaMath.id , GetSolve.id , message.id] , revoke=True)

app.run()