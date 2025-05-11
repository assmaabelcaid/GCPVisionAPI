import os,io
from PIL import Image,ImageDraw
from numpy import random
from pillow_utility import draw_borders,ImageDraw
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'vacca.png'
title = file_name.split('.')
image_path = rf'.\images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image= types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

df = pd.DataFrame(columns=['name','score','bounding_poly'])

for obj in localized_object_annotations:
    new_row = pd.DataFrame(dict(
        name=obj.name,
        score=obj.score,
        bounding_poly=obj.bounding_poly,
    ), index=[0])
    df = pd.concat([df,new_row],ignore_index=True)

pillow_image = Image.open(image_path)
for obj in localized_object_annotations:
    r, g, b = random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)

    draw_borders(pillow_image,obj.bounding_poly,(r,g,b),
                 pillow_image.size, obj.name, obj.score)

pillow_image.save(".\images\detected_images\{0}_detected.png".format(title[0]))
pillow_image.show()

