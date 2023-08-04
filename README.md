# Captcha Generator
  <br>
  <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/CaptchaGenerator-1.1.4-Green" ></a>
  <a href="https://pypi.org/project/Pyrogram/"><img src="https://img.shields.io/badge/pyrogram-2.0.106-orange" ></a>
  <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/Pillow-9.4.0-red" ></a>
  
  
<br><br>

## About Project
### The project is designed for Captcha telegram robot to make it easier to authenticate users. <br> Of course you can use this project elsewhere and this project is not just for telegram robots.
<br><br>

## Install 
### 
<br>
You Can Get Project From pip use this command : 
<br><br>

```
pip install CaptchaGenerator
```
After if you using windows go to files project open fonts folder and install all fonts.

<br>

## How To Work?
### This library has 2 function for Captcha Generator:
   * 1- CaptchaGenerat
       * Numbergen
       * ValueScaptcha
       * NameExport
       * PathEXport
       * Fonts
       * Colors
       * Backgrounds
   * 2- CaptchaGeneratRandom
      * Numbergen
      * ValueScaptcha
      * NUMBERVARIANTS
      * Backgrounds
      * Fonts
      * NameExport
      * PATHEXport
<br>
#### <strong>In order not to create the Capcha Bug process, it was removed from the project. But you can still download this link and download your font.</strong>
<br><br>

## Example CaptchaGenerat :
```python
from CaptchaGenerator.CaptchaGenerator import CaptchaGenerat
def main():
    NumberGen = 5
    NameExport = "CaptchaGenerat"  
    ValuesCaptcha = "012356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%&*"  
    PathExport = r"C:\Path" 
    Fonts = ["fonts/BrunoAce-Regular.ttf" , "fonts/AmaticSC-Bold.ttf"]['AmaticSC-Bold.ttf', 'AmaticSC-Regular.ttf', 'ArchitectsDaughter-Regular.ttf']
    Colors = ["red" , "blue"] 
    Backgrounds = ["C:/Path/Background1.png", "C:/Path/Background2.png", "C:/Path/Background3.png"]
    choiceFromValues = CaptchaGenerat(NumberGen=NumberGen, ValuesCaptcha=ValuesCaptcha, NameExport=NameExport, PathExport=PathExport, Fonts=Fonts, Colors=Colors, Backgrounds=Backgrounds)
    print("Generated captcha : " + choiceFromValues)
if __name__ == "__main__":
    main()
```
## Example CaptchaGenerat In Telegram (Pyrogram) :
<br>

```python
from pyrogram import Client
from pyrogram.types import Message
from CaptchaGenerator.CaptchaGenerator import CaptchaGenerat
import pyromod

app = Client(
    'app', 
    api_id=123, # API ID
    api_hash="", # API HASH
    bot_token="" # BOT Token
)
@app.on_message()
async def start(client : Client , message : Message):
    if message.text == "/start":
        await message.reply_text("Welcome to my bot")
        choiceFromValues = CaptchaGenerat(NumberGen=5 , NumberGen = 5
        NameExport = "CaptchaGenerat"  
        ValuesCaptcha = "012356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%&*"  
        PathExport = r"C:\Path" 
        Fonts = ["fonts/BrunoAce-Regular.ttf" , "fonts/AmaticSC-Bold.ttf"]['AmaticSC-Bold.ttf', 'AmaticSC-Regular.ttf', 'ArchitectsDaughter-Regular.ttf']
        Colors = ["red" , "blue"] 
        Backgrounds = ["C:/Path/Background1.png", "C:/Path/Background2.png", "C:/Path/Background3.png"]
        choiceFromValues = CaptchaGenerat(NumberGen=NumberGen, ValuesCaptcha=ValuesCaptcha, NameExport=NameExport, PathExport=PathExport, Fonts=Fonts, Colors=Colors, Backgrounds=Backgrounds))
        await message.reply_photo(photo=r"c:\path\TelegramCaptcha.png")
        Captcha = await message.chat.ask("For use a bot send captcha :")
        if Captcha.text == choiceFromValues:
            await message.reply_text("Captcha it's true\nWelcome To Bot")
        else:
            await message.reply_text("Capcha is not right\nTry Again /start")
app.run()
```
## Example CaptchaGeneratRandom :
<br>

```python
from CaptchaGenerator.CaptchaGenerator import CaptchaGeneratRandom
def main():
    NumberGen = 5
    NameExport = "CaptchaGenerat"  
    ValuesCaptcha = "012356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%&*"  
    PathExport = r"C:\Path" 
    Fonts = ["fonts/BrunoAce-Regular.ttf" , "fonts/AmaticSC-Bold.ttf"]
    Backgrounds = ["C:/Path/Background1.png", "C:/Path/Background2.png", "C:/Path/Background3.png"]
    correct_answer, variants = CaptchaGeneratRandom(NumberGen=NumberGen , ValuesCaptcha=ValuesCaptcha , NumberVariants=5 , Backgrounds=Backgrounds , Fonts=Fonts , NameExport=NameExport , PathExport=PathExport)
    print("correct answer : " , correct_answer)
    print("variants : " , variants)
if __name__ == "__main__":
    main()
```

## Example CaptchaGeneratRandom In Telegram (Pyrogram) :
<br>

```python
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
```

## Image CaptchaGenerat in Telegram(Pyrogram) :
![Image1](https://raw.githubusercontent.com/Sepehr0Day/CaptchaGenerator/main/TestTelegramBot.png)
## Vidoe Test CaptchaGeneratRandom in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/35b31a23-5786-4762-bb5c-d27651486d67

# By <a href="https://t.me/sepehr0day">Sepehr0Day</a>
## update in coming...
