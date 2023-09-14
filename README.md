# Captcha Generator
  <br>
  <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/CaptchaGenerator-1.1.6-Green" ></a>
  <a href="https://pypi.org/project/Pyrogram/"><img src="https://img.shields.io/badge/pyrogram-2.0.106-orange" ></a>
  <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/Pillow-9.4.0-red" ></a>
  <a href="https://pypi.org/project/gTTS/"><img src="https://img.shields.io/badge/gTTS-2.3.2-blue" ></a> 
  
  
  
<br><br>

## About Project
### The project is designed for Captcha telegram robot to make it easier to authenticate users. <br> Of course you can use this project elsewhere and this project is not just for telegram robots.
<a href="https://github.com/Sepehr0Day/CaptchaGenerator/blob/main/README-FA.md">برای خواندن داکیومنت فارسی اینجا کلیک کنید.</a> 
<br><br>

## Install 
### 
<br>
You Can Get Project From pip use this command : 
<br><br>

```
pip install CaptchaGenerator
```

<br>

## How To Work?
### This library has 3 function for Captcha Generator:
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
      * PathExport
   * 3- CaptchaGeneratorImageRandom (Only Use In Bots)
      * PathFolder
      * NumberRandomSelect
   * 4- CaptchaGeneratorImageDirectionRandom (CaptchaGeneratorIDR) (Only Use In Bots)
      * FolderImagesAddress
   * 5- CaptchaGeneratorAudio (Only Use In Bots)
      * NumberGen
      * ValuesCaptcha
      * NameExport 
      * PathExport
   * 6- CaptchaGeneratorMath (Only Use In Bots)
      *  Not have argument
   * 7- CaptchaGeneratRandomWord (Only Use In Bots)
      * Backgrounds
      * PathWords 
      * Fonts 
      * FontSize 
      * NameExport 
      * PathExport
<br>

### <a href="https://raw.githubusercontent.com/Sepehr0Day/CaptchaGenerator/main/Requirement%20Resources.rar">You can download files requirement resources from here</a>

## Example CaptchaGenerat :
```python
from CaptchaGenerator.CaptchaGenerator import Captcha
def main():
    NumberGen = 5
    NameExport = "CaptchaGenerat"  
    ValuesCaptcha = "012356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%&*"  
    PathExport = r"C:\Path" 
    Fonts = ["fonts/BrunoAce-Regular.ttf" , "fonts/AmaticSC-Bold.ttf"]['AmaticSC-Bold.ttf', 'AmaticSC-Regular.ttf', 'ArchitectsDaughter-Regular.ttf']
    Colors = ["red" , "blue"] 
    Backgrounds = ["C:/Path/Background1.png", "C:/Path/Background2.png", "C:/Path/Background3.png"]
    choiceFromValues = Captcha.CaptchaGenerat(NumberGen=NumberGen, ValuesCaptcha=ValuesCaptcha, NameExport=NameExport, PathExport=PathExport, Fonts=Fonts, Colors=Colors, Backgrounds=Backgrounds)
    print("Generated captcha : " + choiceFromValues)
if __name__ == "__main__":
    main()
```
<br>

## Example CaptchaGeneratRandom :


```python
from CaptchaGenerator.CaptchaGenerator import Captcha
def main():
    NumberGen = 5
    NameExport = "CaptchaGenerat"  
    ValuesCaptcha = "012356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%&*"  
    PathExport = r"C:\Path" 
    Fonts = ["fonts/BrunoAce-Regular.ttf" , "fonts/AmaticSC-Bold.ttf"]
    Backgrounds = ["C:/Path/Background1.png", "C:/Path/Background2.png", "C:/Path/Background3.png"]
    correct_answer, variants = Captcha.CaptchaGeneratRandom(NumberGen=NumberGen , ValuesCaptcha=ValuesCaptcha , NumberVariants=5 , Backgrounds=Backgrounds , Fonts=Fonts , NameExport=NameExport , PathExport=PathExport)
    print("correct answer : " , correct_answer)
    print("variants : " , variants)
if __name__ == "__main__":
    main()
```
## You can see examples code for pyrogram in Examples folder <a href="">here</a>

## Image CaptchaGenerat in Telegram(Pyrogram) :
![Image1](https://raw.githubusercontent.com/Sepehr0Day/CaptchaGenerator/main/TestTelegramBot.png)
## Vidoe Test CaptchaGeneratRandom in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/35b31a23-5786-4762-bb5c-d27651486d67
## Image CaptchaGeneratorImageRandom in Telegram(Pyrogram) :
![Image2](https://raw.githubusercontent.com/Sepehr0Day/CaptchaGenerator/main/TestCaptchaGeneratorImageRandom.png)
## Vidoe Test CaptchaGeneratorImageDirectionRandom in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/b6075908-0f42-4673-b02d-8dd04200952e
## Vidoe Test CaptchaGeneratorAudio in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/dcd203c8-a3db-4152-a24e-2694fba0cb8b
## Vidoe Test CaptchaGeneratorMath in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/a3e84e0d-3749-49e4-8d11-50ce53618551
## Vidoe Test CaptchaGeneratRandomWord in Telegram(Pyrogram) :
https://github.com/Sepehr0Day/CaptchaGenerator/assets/61628516/ebd9aa1c-4d6b-48fb-8048-1037bfa42cb1
# By <a href="https://t.me/sepehr0day">Sepehr0Day</a>

## update in coming...
