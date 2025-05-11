import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import proto

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'

client = vision.ImageAnnotatorClient()

img_url = 'https://media1.tenor.com/m/olJVCiR_oeEAAAAd/brain-rot-isaac.gif'
image = types.Image()
image.source.image_uri = img_url
response = client.text_detection(image=image)

df = pd.DataFrame(columns=['locale', 'description'])

data = []
for text in response.text_annotations:
    data.append({'locale': text.locale, 'description': text.description})

df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

