import os,io
from detectText_local import response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

def cropHint(file_path, aspect_ratio):

    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    crop_hints_params = types.CropHintsParams(aspect_ratios=aspect_Ratios)
    image_context = types.ImageContext(
        crop_hints_params=crop_hints_params
        )
    response = client.crop_hints(image=image, image_context=image_context)

    cropHints = response.crop_hints_annotation.crop_hints
    for crophint in cropHints:
        print('Confidence: ',crophint.confidence)
        print('Importance factor: ', crophint.importance_fraction)
        print('vertices:',crophint.bounding_poly)


file_path = r'.\images\brrbrrpatapim.png'
aspect_Ratios =  [16/9]
cropHint(file_path,aspect_Ratios)