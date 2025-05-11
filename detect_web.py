import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'vacca.png'
image_path = os.path.join('.\images',file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image= types.Image(content=content)
response = client.web_detection(image=image)
web_detection = response.web_detection

print(web_detection.best_guess_labels)
print(web_detection.full_matching_images)
print(web_detection.pages_with_matching_images)
print(web_detection.partial_matching_images)
print(web_detection.visually_similar_images)

for entity in web_detection.web_entities:
    print(entity.description)
    print(entity.score)
    print('-'*50)