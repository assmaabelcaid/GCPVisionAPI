import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

def detect_landmarks(file_path):
    try:
        with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.landmark_detection(image=image)

        landmarks = response.landmark_annotations

        df = pd.DataFrame(columns=['description','score','locations'])

        for landmark in landmarks:
            new_row = pd.DataFrame(dict(
                description=landmark.description,
                score=landmark.score,
                locations=landmark.locations
                ),index=[0])
            df = pd.concat([df, new_row], ignore_index=True)
        return df
    except Exception as e:
        print(e)

file_name = 'stbasil.jpg'
image_path = rf'.\images\landmarks\{file_name}'
detect_landmarks(image_path)