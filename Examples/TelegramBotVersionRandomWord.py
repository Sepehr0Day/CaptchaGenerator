import pyromod , os
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
            NameExport = "CaptchaGenerat"  
            PathExport = path 
            Fonts = [f"{path}fonts/BrunoAce-Regular.ttf" , f"{path}fonts/AmaticSC-Bold.ttf"]
            Backgrounds = [f"{path}/Background/Background2.png", f"{path}/Background/Background2.png", f"{path}/Background/Background2.png"]
            CorrectAnswer = Captcha.CaptchaGeneratRandomWord(Backgrounds=Backgrounds , PathWords=f"{path}\words.txt" , Fonts=Fonts , FontSize=500 , NameExport=NameExport , PathExport=PathExport)
            CaptchaSend =  await message.reply_photo(photo=f"{path}/{NameExport}.png")
            print(CorrectAnswer)
            GetCorrectAnswer = await message.chat.ask("Please Write Text Into Image : ")
            if GetCorrectAnswer.text == CorrectAnswer:
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaSend.id])
                await message.reply_text("Captcha Is True\nWelcome To My Bot")
                data_user.append(message.from_user.id)
            else:
                await app.delete_messages(chat_id=message.chat.id , message_ids=[CaptchaSend.id])
                await message.reply_text("Captcha Is Wrong!!\n/start Again")


app.run()