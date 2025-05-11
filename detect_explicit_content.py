import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'trallalero.png'
image_path = os.path.join('.\images',file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image= types.Image(content=content)
response = client.safe_search_detection(image=image)
safe_search = response.safe_search_annotation

likelihood = ('Uknown','Very unlikely','Unlikely','Possible','Likely','Very Likely')
print('adult: {0}'.format(likelihood[safe_search.adult]))
print('spoof: {0}'.format(likelihood[safe_search.spoof]))
print('medical: {0}'.format(likelihood[safe_search.medical]))
print('violence: {0}'.format(likelihood[safe_search.violence]))
print('racy: {0}'.format(likelihood[safe_search.racy]))