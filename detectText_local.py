import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import proto

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'

client = vision.ImageAnnotatorClient()

FILE_NAME = 'ballerina.png'
FOLDER_PATH = r'C:\Users\Assmaa\Documents\Python_projects\GCPVisionApiDemo\images'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.text_detection(image=image)
df = pd.DataFrame(columns=['locale', 'description'])

data = []
for text in response.text_annotations:
    data.append({'locale': text.locale, 'description': text.description})

df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

print(df['description'][0])


# def detect_text(img): #funzione che prende in input path e nome file e ti restituisce array di parole estratte
#     with io.open(img, 'rb') as image_file:
#         content = image_file.read()
#
#     image = types.Image(content=content)
#     response = client.text_detection(image=image)
#     df = pd.DataFrame(columns=['locale', 'description'])
#
#     data = []
#     for text in response.text_annotations:
#         data.append({'locale': text.locale, 'description': text.description})
#
#     df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
#     return df
#
# FILE_NAME = 'vacca.png'
# FOLDER_PATH = r'C:\Users\Assmaa\Documents\Python_projects\GCPVisionApiDemo\images'
# print(detect_text(os.path.join(FOLDER_PATH, FILE_NAME)))