import os,io

from detectText_local import FOLDER_PATH, response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import proto

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'

client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'C:\Users\Assmaa\Documents\Python_projects\GCPVisionApiDemo\images\handwritten'
IMAGE_FILE = 'text.png'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.document_text_detection(image)

docText = response.full_text_annotation.text
print(docText)


pages = response.full_text_annotation.pages
for page in pages:
    for block in page.blocks:
        print('block condifenzzz ',block.confidence)

        for paragraph in block.paragraphs:
            print('paragraph condifenzzz ',paragraph.confidence)

            for word in paragraph.words:
                word_text = ''.join([symbol.text for symbol in word.symbols])

                print('Word text: {0} (confidence: {1})'.format(word_text, word.confidence))

                for symbol in word.symbols:
                    print('\tsymbol: {0}(confidence: {1}'.format(symbol.text, symbol.confidence))

# COSA HO SCOPERTO: Per l'immagine live laugh love se l'immagine è invertita di 180*
# confidenc interval =
# Word text: love (confidence: 0.9749397039413452)
# 	symbol: l(confidence: 0.9175840616226196
# 	symbol: o(confidence: 0.9881165623664856
# 	symbol: v(confidence: 0.9957367181777954
# 	symbol: e(confidence: 0.9983214735984802
#
# se invece è normale:
# Word text: love (confidence: 0.9594225883483887)
# 	symbol: l(confidence: 0.8509789109230042
# 	symbol: o(confidence: 0.9884873032569885
# 	symbol: v(confidence: 0.998852550983429
# 	symbol: e(confidence: 0.9993715882301331
#
# Per immagine stop being female:
# normale e invertita = confidence interval

# Per immagine handwritten:
# normale:
# Word text: Text (confidence: 0.9698569774627686)
# 	symbol: T(confidence: 0.9159449934959412
# 	symbol: e(confidence: 0.9883089661598206
# 	symbol: x(confidence: 0.9830547571182251
# 	symbol: t(confidence: 0.9921191334724426
# invertita:
# Word text: Text (confidence: 0.9727109670639038)
# 	symbol: T(confidence: 0.9718384146690369
# 	symbol: e(confidence: 0.9891707897186279
# 	symbol: x(confidence: 0.9386675357818604
# 	symbol: t(confidence: 0.9911670088768005
