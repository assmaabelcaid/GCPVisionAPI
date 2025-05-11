import os,io
from PIL import Image,ImageDraw,  ImageFont
from google.cloud import vision
from google.cloud.vision_v1 import types
from draw_vertice import drawVertices
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'mm.png'
image_path = rf'.\images\logos\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.logo_detection(image=image)
logos = response.logo_annotations

df = pd.DataFrame(columns=['description','score'])
for logo in logos:
    # new_row = pd.DataFrame(dict(
    #     description=logo.description,
    #     score=logo.score
    # ), index=[0])
    # df = pd.concat([df, new_row], ignore_index=True)
    #print(df)
    #------------ nice table

    print(logo.description)
    print(logo.score)
    print('-'*50)
    vertices = [(v.x, v.y) for v in logo.bounding_poly.vertices]
    print('Vertices values {0}'.format(vertices))

    #suppose i wanna make a function to draw a poligon around the detected logo
    image_pil = Image.open(image_path)
    draw = ImageDraw.Draw(image_pil)
    draw.polygon(vertices, outline=(0, 127, 0), width=6)

    image_pil.show()

    #suppose instead i wanna draw with another function (from tutorial)

    drawVertices(content, vertices, logo.description)