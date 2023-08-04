from PIL import Image, ImageDraw, ImageFont
from colorama import Fore
from ColorsCap.ColorsCap import color_dict
import random , os


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

def CaptchaGenerat(NumberGen=None, ValuesCaptcha=None, NameExport=None,  PathExport=None, Fonts=None, Colors=None, Backgrounds=None):
    
    if NumberGen is None or ValuesCaptcha is None or NameExport is None or PathExport is None or Fonts is None  or Colors is None or Backgrounds is None :
        raise ValueError(Fore.RED+"All argument is required."+Fore.WHITE)
    else:

          img = Image.open(random.choice(Backgrounds)).convert("RGBA")
          font = ImageFont.truetype(random.choice(Fonts), 1000)
          values = ValuesCaptcha
          choiceFromValues = "".join(random.sample(values, int(NumberGen)))

          draw = ImageDraw.Draw(img)
          textwidth, textheight = draw.textsize(choiceFromValues, font)
          width, height = img.size
          x = (width - textwidth) / 2
          y = (height - textheight) / 2
          draw.text((x, y), choiceFromValues, font=font, fill=random.choice(Colors))
          line_color = random.choice(list(color_dict.keys()))
          num_lines = random.randint(20, 35)
          for i in range(num_lines):
              line_width = random.randint(20, 30)
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
          img.save(f"{PathExport}/{NameExport}.png")
          return choiceFromValues

def CaptchaGeneratRandom(NumberGen=None , ValuesCaptcha=None , NumberVariants=None, Backgrounds=None , Fonts=None , NameExport=None,  PathExport=None):
    if NumberGen is None or ValuesCaptcha is None or NumberVariants is None or Backgrounds is None or Fonts is None or NameExport is None or PathExport is None :
        raise ValueError(Fore.RED+"All argument is required."+Fore.WHITE)
    else:
        img = Image.open(random.choice(Backgrounds)).convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        variants = []
        for _ in range(NumberVariants):
            variant = ''.join(random.choice(ValuesCaptcha) for _ in range(NumberGen))
            variants.append(variant)
        font = ImageFont.truetype(random.choice(Fonts), 1000)
        correct_answer = random.choice(variants)
        textwidth, textheight = draw.textsize(correct_answer, font)
        width, height = img.size
        x = (width - textwidth) / 2
        y = (height - textheight) / 2

        for _ in range(50):
            line_color = random.choice(list(color_dict.keys()))
            line_width = random.randint(15, 35)
            start_point = (random.randint(0, width), random.randint(0, height))
            end_point = (random.randint(0, width), random.randint(0, height))
            draw.line([start_point, end_point], fill=line_color, width=line_width)

        for _ in range(29):
            scratch_color = random.choice(list(color_dict.keys()))
            scratch_width = random.randint(15, 50)
            scratch_height = random.randint(50, 70)
            scratch_left = random.randint(0, width - scratch_width)
            scratch_top = random.randint(0, height - scratch_height)
            scratch_right = scratch_left + scratch_width
            scratch_bottom = scratch_top + scratch_height
            draw.rectangle((scratch_left, scratch_top, scratch_right, scratch_bottom), outline=scratch_color)

        char_spacing = 4 
        char_font = ImageFont.truetype(random.choice(Fonts), 800)
        char_height = char_font.getsize(correct_answer)[1] 
        char_y = (height - char_height) / 2 
        x = (width - textwidth) / 2
        for char in correct_answer:
           char_width, _ = draw.textsize(char, font=char_font)
           draw.text((x, char_y), char, font=char_font, fill=random.choice(list(color_dict.keys())))
           x += char_width + char_spacing
           draw_random_circle(draw, width, height)
           draw_random_rectangle(draw, width, height)
           draw_random_square(draw, width, height)
           draw_random_triangle(draw, width, height)

        img.save(f"{PathExport}/{NameExport}.png")
        return correct_answer, variants
    
