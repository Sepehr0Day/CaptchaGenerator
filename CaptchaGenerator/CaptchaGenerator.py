from PIL import Image, ImageDraw, ImageFont
from colorama import Fore
from gtts import gTTS
import random , os
color_dict = {
    "aliceblue": (240, 248, 255),
    "antiquewhite": (250, 235, 215),
    "aqua": (0, 255, 255),
    "aquamarine": (127, 255, 212),
    "azure": (240, 255, 255),
    "beige": (245, 245, 220),
    "bisque": (255, 228, 196),
    "black": (0, 0, 0),
    "blanchedalmond": (255, 235, 205),
    "blue": (0, 0, 255),
    "blueviolet": (138, 43, 226),
    "brown": (165, 42, 42),
    "burlywood": (222, 184, 135),
    "cadetblue": (95, 158, 160),
    "chartreuse": (127, 255, 0),
    "chocolate": (210, 105, 30),
    "coral": (255, 127, 80),
    "cornflowerblue": (100, 149, 237),
    "cornsilk": (255, 248, 220),
    "crimson": (220, 20, 60),
    "cyan": (0, 255, 255),
    "darkblue": (0, 0, 139),
    "darkcyan": (0, 139, 139),
    "darkgoldenrod": (184, 134, 11),
    "darkgray": (169, 169, 169),
    "darkgrey": (169, 169, 169),
    "darkgreen": (0, 100, 0),
    "darkkhaki": (189, 183, 107),
    "darkmagenta": (139, 0, 139),
    "darkolivegreen": (85, 107, 47),
    "darkorange": (255, 140, 0),
    "darkorchid": (153, 50, 204),
    "darkred": (139, 0, 0),
    "darksalmon": (233, 150, 122),
    "darkseagreen": (143, 188, 143),
    "darkslateblue": (72, 61, 139),
    "darkslategray": (47, 79, 79),
    "darkslategrey": (47, 79, 79),
    "darkturquoise": (0, 206, 209),
    "darkviolet": (148, 0, 211),
    "deeppink": (255, 20, 147),
    "deepskyblue": (0, 191, 255),
    "dimgray": (105, 105, 105),
    "dimgrey": (105, 105, 105),
    "dodgerblue": (30, 144, 255),
    "firebrick": (178, 34, 34),
    "floralwhite": (255, 250, 240),
    "forestgreen": (34, 139, 34),
    "fuchsia": (255, 0, 255),
    "gainsboro": (220, 220, 220),
    "ghostwhite": (248, 248, 255),
    "gold": (255, 215, 0),
    "goldenrod": (218, 165, 32),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),
    "green": (0, 128, 0),
    "greenyellow": (173, 255, 47),
    "honeydew": (240, 255, 240),
    "hotpink": (255, 105, 180),
    "indianred": (205, 92, 92),
    "indigo": (75, 0, 130),
    "ivory": (255, 255, 240),
    "khaki": (240, 230, 140),
    "lavender": (230, 230, 250),
    "lavenderblush": (255, 240, 245),
    "lawngreen": (124, 252, 0),
    "lemonchiffon": (255, 250, 205),
    "lightblue": (173, 216, 230),
    "lightcoral": (240, 128, 128),
    "lightcyan": (224, 255, 255),
    "lightgoldenrodyellow": (250, 250, 210),
    "lightgreen": (144, 238, 144),
    "lightgray": (211, 211, 211),
    "lightgrey": (211, 211, 211),
    "lightpink": (255, 182, 193),
    "lightsalmon": (255, 160, 122),
    "lightseagreen": (32, 178, 170),
    "lightskyblue": (135, 206, 250),
    "lightslategray": (119, 136, 153),
    "lightslategrey": (119, 136, 153),
    "lightsteelblue": (176, 196, 222),
    "lightyellow": (255, 255, 224),
    "lime": (0, 255, 0),
    "limegreen": (50, 205, 50),
    "linen": (250, 240, 230),
    "magenta": (255, 0, 255),
    "maroon": (128, 0, 0),
    "mediumaquamarine": (102, 205, 170),
    "mediumblue": (0, 0, 205),
    "mediumorchid": (186, 85, 211),
    "mediumpurple": (147, 112, 219),
    "mediumseagreen": (60, 179, 113),
    "mediumslateblue": (123, 104, 238),
    "mediumspringgreen": (0, 250, 154),
    "mediumturquoise": (72, 209, 204),
    "mediumvioletred": (199, 21, 133),
    "midnightblue": (25, 25, 112),
    "mintcream": (245, 255, 250),
    "mistyrose": (255, 228, 225),
    "moccasin": (255, 228, 181),
    "navajowhite": (255, 222, 173),
    "navy": (0, 0, 128),
    "oldlace": (253, 245, 230),
    "olive": (128, 128, 0),
    "olivedrab": (107, 142, 35),
    "orange": (255, 165, 0),
    "orangered": (255, 69, 0),
    "orchid": (218, 112, 214),
    "palegoldenrod": (238, 232, 170),
    "palegreen": (152, 251, 152),
    "paleturquoise": (175, 238, 238),
    "palevioletred": (219, 112, 147),
    "papayawhip": (255, 239, 213),
    "peachpuff": (255, 218, 185),
    "peru": (205, 133, 63),
    "pink": (255, 192, 203),
    "plum": (221, 160, 221),
    "powderblue": (176, 224, 230),
    "purple": (128, 0, 128),
    "rebeccapurple": (102, 51, 153),
    "red": (255, 0, 0),
    "rosybrown": (188, 143, 143),
    "royalblue": (65, 105, 225),
    "saddlebrown": (139, 69, 19),
    "salmon": (250, 128, 114),
    "sandybrown": (244, 164, 96),
    "seagreen": (46, 139, 87),
    "seashell": (255, 245, 238),
    "sienna": (160, 82, 45),
    "silver": (192, 192, 192),
    "skyblue": (135, 206, 235),
    "slateblue": (106, 90, 205),
    "slategray": (112, 128, 144),
    "slategrey": (112, 128, 144),
    "snow": (255, 250, 250),
    "springgreen": (0, 255, 127),
    "steelblue": (70, 130, 180),
    "tan": (210, 180, 140),
    "teal": (0, 128, 128),
    "thistle": (216, 191, 216),
    "tomato": (255, 99, 71),
    "turquoise": (64, 224, 208),
    "violet": (238, 130, 238),
    "wheat": (245, 222, 179),
    "white": (255, 255, 255),
    "whitesmoke": (245, 245, 245),
    "yellow": (255, 255, 0),
    "yellowgreen": (154, 205, 50)
}
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

class Captcha:
    @staticmethod
    def CaptchaGenerat(NumberGen=None, ValuesCaptcha=None, NameExport=None, PathExport=None, Fonts=None, Colors=None, Backgrounds=None):
        if NumberGen is None or ValuesCaptcha is None or NameExport is None or PathExport is None or Fonts is None or Colors is None or Backgrounds is None:
            raise ValueError(Fore.RED + "All arguments are required." + Fore.WHITE)
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

    @staticmethod
    def CaptchaGeneratRandom(NumberGen=None, ValuesCaptcha=None, NumberVariants=None, Backgrounds=None, Fonts=None, NameExport=None, PathExport=None):
        if NumberGen is None or ValuesCaptcha is None or NumberVariants is None or Backgrounds is None or Fonts is None or NameExport is None or PathExport is None:
            raise ValueError(Fore.RED + "All arguments are required." + Fore.WHITE)
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

    @staticmethod
    def CaptchaGeneratorImageRandom(PathFolder, NumberRandomSelect):
        ImageList = []
        for filename in os.listdir(PathFolder):
            if os.path.isfile(os.path.join(PathFolder, filename)):
                name, extension = os.path.splitext(filename)
                if extension.lower() in ['.jpg', '.png']:
                    ImageList.append(filename)

        RandomImageList = random.sample(ImageList, int(NumberRandomSelect))
        ImageSelected = random.choice(RandomImageList)
        ImageSelectedName, ImageSelectedFormat = os.path.splitext(ImageSelected)
        ImageNamesInFolder = [os.path.splitext(image)[0] for image in RandomImageList]

        return ImageSelected, ImageSelectedName, ImageSelectedFormat, ImageNamesInFolder

    @staticmethod
    def CaptchaGeneratorIDR(FolderImagesAddress=None):
        Images = ""
        if FolderImagesAddress:
            Images = FolderImagesAddress
        else:
            Images = __file__

        script_directory = os.path.dirname(os.path.abspath(Images))
        image_formats = {'.png', '.jpg', '.jpeg'}
        image_list = [entry.name for entry in os.scandir(script_directory) if entry.is_file() and entry.name.endswith(tuple(image_formats))]

        directions = {
            '⬆️': ['Up'],
            '⬇️': ['Bottom'],
            '⬅️': ['Left'],
            '➡️': ['Right'],
            '↗️': ['UpRight'],
            '↘️': ['BottomRight'],
            '↙️': ['BottomLeft'],
            '↖️': ['UpLeft']
        }

        random_image = random.choice(image_list)
        random_direction = None

        for direction_icon, direction_names in directions.items():
            for direction in direction_names:
                if direction in random_image:
                    random_direction = direction_icon
                    break

        direction_text = {
            '⬆️': 'Up',
            '⬇️': 'Down',
            '⬅️': 'Left',
            '➡️': 'Right',
            '↗️': 'UpRight',
            '↘️': 'DownRight',
            '↙️': 'DownLeft',
            '↖️': 'UpLeft'
        }.get(random_direction, '')
        return random_image, direction_text
    
    @staticmethod
    def CaptchaGeneratorAudio(NumberGen=None, ValuesCaptcha=None, NameExport=None, PathExport=None):
        if None in (NumberGen, ValuesCaptcha, NameExport, PathExport):
            raise ValueError(Fore.RED + "All arguments are required." + Fore.WHITE)
        else:
            captchavalue = [random.choice(ValuesCaptcha) for _ in range(int(NumberGen))]
            captchas_text = ','.join(captchavalue)
            captcha = ''.join(captchavalue)
            captchas_with_commas = ','.join(list(captchas_text))
            tts = gTTS(text=captchas_with_commas, lang='en')
            captcha_filename = f'{PathExport}/{NameExport}.mp3'
            tts.save(captcha_filename)
            return captcha , captcha_filename
        
    @staticmethod
    def CaptchaGeneratorMath():
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10) 
        operator = random.choice(['+', '-', '*'])
        operator_functions = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
            }    
        result = operator_functions[operator](num1, num2)
        captcha = f"{num1} {operator} {num2}"    
        return captcha, result
    
    @staticmethod
    def CaptchaGeneratRandomWord(Backgrounds=None, PathWords=None , Fonts=None, FontSize=None , NameExport=None, PathExport=None):
        if Backgrounds is None or Fonts is None or FontSize is None or NameExport is None or PathExport is None or PathWords is None:
            raise ValueError(Fore.RED + "All arguments are required." + Fore.WHITE)
        else:
            img = Image.open(random.choice(Backgrounds)).convert("RGBA")
            draw = ImageDraw.Draw(img)
            words = []
            with open(f"{PathWords}") as file:
                for line in file:
                    word = line.strip()
                    words.append(word)
                file.close()
            font = ImageFont.truetype(random.choice(Fonts), int(FontSize))
            correct_answer = random.choice(words) 
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
            char_font = ImageFont.truetype(random.choice(Fonts), int(FontSize))
            char_width, char_height = draw.textsize(correct_answer, font=char_font)
            char_y = (height - char_height) / 2
            x = (width - (char_width + (len(correct_answer) - 1) * char_spacing)) / 2
            for char in correct_answer:
                char_width, _ = draw.textsize(char, font=char_font)
                draw.text((x, char_y), char, font=char_font, fill=random.choice(list(color_dict.keys())))
                x += char_width + char_spacing
                draw_random_circle(draw, width, height)
                draw_random_rectangle(draw, width, height)
                draw_random_square(draw, width, height)
                draw_random_triangle(draw, width, height)

            img.save(f"{PathExport}/{NameExport}.png")
            return correct_answer