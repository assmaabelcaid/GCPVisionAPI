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
response = client.label_detection(image=image)
labels = response.label_annotations

df = pd.DataFrame(columns=['description','score','topicality'])
for label in labels:
    new_row = pd.DataFrame(dict(
        description=label.description,
        score=label.score,
        topicality=label.topicality,
    ), index=[0])  # Added index=[0] here
    df = pd.concat([df, new_row], ignore_index=True)


print(df)