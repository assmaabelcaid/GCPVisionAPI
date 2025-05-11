import os,io

from detectText_local import response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = 'emotions.png'
image_path = rf'.\images\faces\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.face_detection(image=image)
faceAnnotation = response.face_annotations

likelihood = ('Uknown','Very Unlikely','Unlikely','Possibly','Likely','Very Likely')

print('Faces:')
for face in faceAnnotation:
    print('Detection confidence: {0}'.format(face.detection_confidence))
    print('Angry likelihood: {0}'.format(likelihood[face.anger_likelihood]))
    print('Joy likelihood: {0}'.format(likelihood[face.joy_likelihood]))
    print('Sorrow likelihood: {0}'.format(likelihood[face.sorrow_likelihood]))
    print('Surprise likelihood: {0}'.format(likelihood[face.surprise_likelihood]))
    print('Headwear likelihood: {0}'.format(likelihood[face.headwear_likelihood]))
    face_vertices = ['({0},{1})'.format(vertex.x,vertex.y) for vertex in face.bounding_poly.vertices]
    print('Face bound: {0}'.format(', '.join(face_vertices)))
    print('')

 