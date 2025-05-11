import os,io
import re
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import storage
from google.protobuf import json_format
import json
'''
pip install --upgrade google-cloud-storage
gs://my_pdf/Arbeitgeberbestätigung_Bachelor_4.0_tctze7 en.pdf -- your file from google storage
'''

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'servicAccountToken.json'
client = vision.ImageAnnotatorClient()

batch_size = 2
mime_type = 'application/pdf'
feature = types.Feature(
    type=vision.Feature.Type.DOCUMENT_TEXT_DETECTION
)

gcs_source_uri = 'gs://my_pdf/Arbeitgeberbestätigung_Bachelor_4.0_tctze7 en.pdf'
gcs_source = types.GcsSource(uri=gcs_source_uri)
input_config = types.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

gcs_destination_uri = 'gs://my_pdf/Arbeitgeberbestätigung_Bachelor_4.0_tctze7 en.pdf/pdf_result/'
gcs_destination = types.GcsDestination(uri=gcs_destination_uri)
output_config = types.OutputConfig(gcs_destination=gcs_destination, batch_size=batch_size)

async_request = types.AsyncAnnotateFileRequest(
    features=[feature], input_config=input_config, output_config=output_config)
operation = client.async_batch_annotate_files(requests=[async_request])
operation.result(timeout=180)

#now we need to work with storage api

storage_client = storage.Client()
match = re.match(r'gs://([^/]+)/(.*)', gcs_destination_uri)
bucket_name = match.group(1)
prefix = match.group(2)
bucket = storage_client.get_bucket(bucket_name)

# list object with the given prefix
blob_list = list(bucket.list_blobs(prefix=prefix))
print('Output Files: ')
for blob in blob_list:
    print(blob.name)

# Assuming you want to process the first output file
output_blob = blob_list[0]
json_string = output_blob.download_as_bytes().decode('utf-8')

# Parse the JSON string into a Python dictionary
json_data = json.loads(json_string)
full_text = ""
if "responses" in json_data and json_data["responses"]:
    responses = json_data["responses"]
    number_of_responses = len(responses)
    if "fullTextAnnotation" in json_data["responses"][0]:
        annotation = json_data["responses"][0]["fullTextAnnotation"]
        if "pages" in annotation:
            for page in annotation["pages"]:
                if "blocks" in page:
                    for block in page["blocks"]:
                        if "paragraphs" in block:
                            for paragraph in block["paragraphs"]:
                                if "words" in paragraph:
                                    for word_data in paragraph["words"]:
                                        word = "".join([symbol["text"] for symbol in word_data["symbols"]])
                                        full_text += ' ' + word
                                    full_text += "\n" # Add newline after each paragraph (you might need to adjust this based on your needs)

print("\nExtracted Text:")
print(full_text)