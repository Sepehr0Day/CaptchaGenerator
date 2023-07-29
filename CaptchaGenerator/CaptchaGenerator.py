from PIL import Image, ImageDraw, ImageFont
from Colors.colors import color_dict
from colorama import Fore
import random
def draw_random_circle(draw, width, height):
    circle_color = random.choice(list(color_dict.keys()))
    circle_color_rgb = color_dict.get(circle_color, (0, 0, 0))
    draw.ellipse([(0, 0), (width, height)], outline=circle_color_rgb)

def draw_random_rectangle(draw, width, height):
    rectangle_color = random.choice(list(color_dict.keys()))
    rectangle_width = random.randint(50, width)
    rectangle_height = random.randint(50, height)
    rectangle_left = (width - rectangle_width) // 2
    rectangle_top = (height - rectangle_height) // 2
    rectangle_right = rectangle_left + rectangle_width
    rectangle_bottom = rectangle_top + rectangle_height
    draw.rectangle((rectangle_left, rectangle_top, rectangle_right, rectangle_bottom), outline=rectangle_color)

def draw_random_square(draw, width, height):
    square_color = random.choice(list(color_dict.keys()))
    square_size = random.randint(2, min(width, height))
    square_left = (width - square_size) // 2
    square_top = (height - square_size) // 2
    square_right = square_left + square_size
    square_bottom = square_top + square_size
    draw.rectangle((square_left, square_top, square_right, square_bottom), outline=square_color)

def draw_random_triangle(draw, width, height):
    triangle_color = random.choice(list(color_dict.keys()))
    triangle_size = random.randint(5, min(width, height))
    triangle_top = (height - triangle_size) // 2
    triangle_bottom = triangle_top + triangle_size
    triangle_left = (width - triangle_size) // 2
    triangle_right = triangle_left + triangle_size
    triangle_points = [(triangle_left, triangle_bottom), ((triangle_left + triangle_right) // 2, triangle_top), (triangle_right, triangle_bottom)]
    draw.polygon(triangle_points, outline=triangle_color)

def CaptchaGenerat(NumberGen=None, ValuesCaptcha=None, NameExport=None,  PathExport=None, Fonts=None, Colors=None, BackgroundS=None):
    
    if NumberGen is None:
        raise ValueError(Fore.RED+"NumberGen argument is required."+Fore.WHITE)
    if NameExport is None:
        print(Fore.YELLOW+"NameExport argument is none; so program use name export " + Fore.BLUE + "captcha.png"+Fore.WHITE)
    if PathExport is None:
        raise ValueError(Fore.RED+"PathExport argument is required."+Fore.WHITE)
    if ValuesCaptcha is None:
        print(Fore.YELLOW+"ValuesCaptcha argument is none; so program use a this Values : 12356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm."+Fore.WHITE)
        VSCaptcha = "12356789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    if Fonts is None:
       print(Fore.YELLOW+"Fonts argument is none; so program use a default fonts"+Fore.WHITE)
       fO = ['AmaticSC-Bold.ttf', 'AmaticSC-Regular.ttf', 'ArchitectsDaughter-Regular.ttf', 'BrunoAce-Regular.ttf', 'Cormorant-Italic-VariableFont_wght.ttf', 'Cormorant-VariableFont_wght.ttf', 'Dosis-Bold.ttf', 'Dosis-ExtraBold.ttf', 'Dosis-ExtraLight.ttf', 'Dosis-Light.ttf', 'Dosis-Medium.ttf', 'Dosis-Regular.ttf', 'Dosis-SemiBold.ttf', 'Dosis-VariableFont_wght.ttf', 'Gruppo-Regular.ttf', 'Kalam-Bold.ttf', 'Kalam-Light.ttf', 'Kalam-Regular.ttf', 'Lexend-VariableFont_wght.ttf', 'MateSC-Regular.ttf', 'NotoSansSundanese-Bold.ttf', 'NotoSansSundanese-Medium.ttf', 'NotoSansSundanese-Regular.ttf', 'NotoSansSundanese-SemiBold.ttf', 'NotoSansSundanese-VariableFont_wght.ttf', 'Nunito-VariableFont_wght.ttf', 'Orbitron-Black.ttf', 'Orbitron-Bold.ttf', 'Orbitron-ExtraBold.ttf', 'Orbitron-Medium.ttf', 'Orbitron-Regular.ttf', 'Orbitron-SemiBold.ttf', 'Orbitron-VariableFont_wght.ttf', 'Rajdhani-Bold.ttf', 'Rajdhani-Light.ttf', 'Rajdhani-Medium.ttf', 'Rajdhani-Regular.ttf', 'Rajdhani-SemiBold.ttf', 'Raleway-Black.ttf', 'Raleway-BlackItalic.ttf', 'Raleway-Bold.ttf', 'Raleway-BoldItalic.ttf', 'Raleway-ExtraBold.ttf', 'Raleway-ExtraBoldItalic.ttf', 'Raleway-ExtraLight.ttf', 'Raleway-ExtraLightItalic.ttf', 'Raleway-Italic-VariableFont_wght.ttf', 'Raleway-Italic.ttf', 'Raleway-Light.ttf', 'Raleway-LightItalic.ttf', 'Raleway-Medium.ttf', 'Raleway-MediumItalic.ttf', 'Raleway-Regular.ttf', 'Raleway-SemiBold.ttf', 'Raleway-SemiBoldItalic.ttf', 'Raleway-Thin.ttf', 'Raleway-ThinItalic.ttf', 'Raleway-VariableFont_wght.ttf', 'ShadowsIntoLight-Regular.ttf', 'SpaceMono-Bold.ttf', 'Tektur-Black.ttf', 'Tektur-Bold.ttf', 'Tektur-ExtraBold.ttf', 'Tektur-Medium.ttf', 'Tektur-Regular.ttf', 'Tektur-SemiBold.ttf', 'Tektur-VariableFont_wdth,wght.ttf', 'Tektur_Condensed-Black.ttf', 'Tektur_Condensed-Bold.ttf', 'Tektur_Condensed-ExtraBold.ttf', 'Tektur_Condensed-Medium.ttf', 'Tektur_Condensed-Regular.ttf', 'Tektur_Condensed-SemiBold.ttf', 'Tektur_SemiCondensed-Black.ttf', 'Tektur_SemiCondensed-Bold.ttf', 'Tektur_SemiCondensed-ExtraBold.ttf', 'Tektur_SemiCondensed-Medium.ttf', 'Tektur_SemiCondensed-Regular.ttf', 'Tektur_SemiCondensed-SemiBold.ttf']
    if Colors is None:
        print(Fore.YELLOW+"Colors argument is none; so program use a random color"+Fore.WHITE)
        Co = [(random.choice(list(color_dict.keys())))]
    if BackgroundS is None:
        print(Fore.YELLOW+"BackgroundS argument is none; so program use a default bakcgrounds"+Fore.WHITE)  
        BC = ["Background/Background1.png", "Background/Background2.png", "Background/Background3.png" , "Background/Background4.png" , "Background/Background5.png"] 
    if NumberGen > 6:
        print(Fore.YELLOW+"NumberGen argument is too long; Length can be 1 to 5."+Fore.WHITE)
    else:
          if BackgroundS == None:
             img = Image.open(random.choice(BC)).convert("RGBA")
          else:
              img = Image.open(random.choice(BackgroundS)).convert("RGBA")
          if Fonts == None: 
              font = ImageFont.truetype(random.choice(fO), 1000)
          else:
              font = ImageFont.truetype(random.choice(Fonts), 1000)
          if ValuesCaptcha == None:
              values = VSCaptcha
          else:
              values = ValuesCaptcha

          choiceFromValues = "".join(random.sample(values, int(NumberGen)))

          draw = ImageDraw.Draw(img)
          textwidth, textheight = draw.textsize(choiceFromValues, font)
          width, height = img.size
          x = (width - textwidth) / 2
          y = (height - textheight) / 2
          if Colors == None: 
             draw.text((x, y), choiceFromValues, font=font, fill=random.choice(Co))
          else:
             draw.text((x, y), choiceFromValues, font=font, fill=random.choice(Colors))
          line_color = random.choice(list(color_dict.keys()))
          num_lines = random.randint(10, 20)
          for i in range(num_lines):
              line_width = random.randint(5, 10)
              start_point = (random.randint(0, width), random.randint(0, height))
              end_point = (random.randint(0, width), random.randint(0, height))
              draw.line([start_point, end_point], fill=line_color, width=line_width)
          num_nested_lines = random.randint(10, 20)
          nested_line_color = random.choice(list(color_dict.keys()))
          for i in range(num_nested_lines):
              nested_line_width = random.randint(5, 10)
              nested_start_point = (random.randint(0, width), random.randint(0, height))
              nested_end_point = (random.randint(0, width), random.randint(0, height))
              draw.line([nested_start_point, nested_end_point], fill=nested_line_color, width=nested_line_width)
          draw_random_circle(draw, width, height)
          draw_random_rectangle(draw, width, height)
          draw_random_square(draw, width, height)
          draw_random_triangle(draw, width, height)
          if NameExport == None:   
             img.save(f"{PathExport}/captcha.png")
          else:
              img.save(f"{PathExport}/{NameExport}.png")
          return choiceFromValues


CaptchaGenerat()