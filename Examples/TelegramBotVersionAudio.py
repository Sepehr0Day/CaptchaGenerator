import os , pyromod
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
            path = os.getcwd()
            CaptchaText , CaptchaPath= Captcha.CaptchaGeneratorAudio(5 , "1234567890qwertyuiopasdfghjklzxcvbnm" , "Captcha" , path)            
            CaptchaAudio = await message.reply_audio(audio="Captcha.mp3" , caption="Please enter the content of the audio file")
            GetCaptcha = await message.chat.ask("Enter content : ")
            if GetCaptcha.text == CaptchaText:
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaAudio.id , GetCaptcha.id , message.id] , revoke=True)
                await message.reply_text("Captcha is True\nWelcome To My Bot!")
                data_user.append(message.from_user.id)
            else:
                await message.reply_text("Captcha is Wrong!!\n/start")
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaAudio.id , GetCaptcha.id , message.id] , revoke=True)

app.run()