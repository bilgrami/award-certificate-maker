
import pandas as pd 
from PIL import Image, ImageDraw, ImageFont

BASE_IMAGE = 'images/BalighaCertificate.jpg'

def write_text_on_image(name, dt):
    img = Image.open(BASE_IMAGE)
    d1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('FreeMono.ttf', 7+86)
    name_x = 786-14-5-4-3-2-1
    name_y = 555-14-5-4-3-2-1
    dt_x = 786-14-5-4-3-2-1
    dt_y = 1555-140-5-4-3-2-1

    d1.text((name_x, name_y), name, font=myFont, fill =(0, 0, 0))
    d1.text((dt_x, dt_y), dt, font=myFont, fill =(0, 0, 0))
    # img.show()
    img.save(f"output/cert-{name}.jpg")


df = pd.read_csv("./data/names.csv")
for index, row in df.iterrows():
    print("Generating certificate for " + row['name'])
    write_text_on_image(row['name'], row['date'])
    

