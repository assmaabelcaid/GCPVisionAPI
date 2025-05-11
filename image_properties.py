import os,io

from detectText_local import response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'vacca.png'
image_path = rf'.\images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.image_properties(image).image_properties_annotation

dominant_colors = response.dominant_colors

for color in dominant_colors.colors:
    print('pixel fraction: {0}'.format(color.pixel_fraction))
    print('score value: {0}'.format(color.score))
    print('\tred: {0}'.format(color.color.red))
    print('\tgreen: {0}'.format(color.color.green))
    print('\tblue: {0}'.format(color.color.blue))
    print('')
