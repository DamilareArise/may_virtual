import index as ind

# ind.add()
# father = ind.Father('reading')
# father.intro()

# from index import Father

# father = Father('Reading')
# father.intro()


import time
import datetime as dt
import random as rd

# print('Loading...')
# time.sleep(3)
# print('done')

# print(dt.datetime.now())

# print(rd.randint(1000000000, 1099999999))


import pyttsx3

# pyttsx3.speak('Hello class')

from PIL import Image, ImageDraw, ImageFont

text = 'Hello Everyone'
img = Image.new("RGB", (800, 200), color="white")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((10, 50), text, fill="black", font=font)
img.save('img.png')

