import os
import re
from google.cloud import storage
from google.cloud import texttospeech
from google.cloud import vision
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-key-gcloud.json'
# gs://dados666/test1.pdf
client = vision.ImageAnnotatorClient()


# import packages
# define function that uploads a file from the bucket

def upload_cs_file(destination_file_name, source_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket("dados666")

    blob = bucket.blob(destination_file_name)

    blob.upload_from_filename(source_file_name)

    return True


# def create_bucket(bucket_name, storage_class='STANDARD', location='eu'):
#     """ Create a new bucket"""
#     storage_client = storage.Clien"t()
#
#     bucket = storage_client.bucket(bucket_name)  # Bucket names must start and end with a number or letter.
#     bucket.storage_class = storage_class
#
#     bucket = storage_client.create_bucket(bucket, location="eu")
#
#     return f'Bucket {bucket.name} successfully created.'
# create_bucket("dados666")



def async_detect_document(name_pdf):
    """OCR with PDF/TIFF as source files on GCS"""
    batch_size = 2

    mime_type = 'application/pdf'
    feature = vision.Feature({"type_": vision.Feature.Type.DOCUMENT_TEXT_DETECTION})

    gcs_source_uri = f"gs://dados666/{name_pdf}"
    gcs_source = vision.GcsSource({"uri": gcs_source_uri})
    input_config = vision.InputConfig({"gcs_source": gcs_source, "mime_type": mime_type})

    gcs_destination_uri = f"gs://dados666/547547"                                     # <----- Possible problems
    gcs_destination = vision.GcsDestination({"uri": gcs_destination_uri})
    output_config = vision.OutputConfig({"gcs_destination": gcs_destination, "batch_size": batch_size})

    async_request = vision.AsyncAnnotateFileRequest(
        {"features": [feature], "input_config": input_config, "output_config": output_config})

    operation = client.async_batch_annotate_files(requests=[async_request])
    print('Waiting for the operation to finish.')
    operation.result(timeout=180)

    # Once the request has completed and the output has been
    # written to GCS, we can list all the output files.
    storage_client = storage.Client()
    match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
    bucket_name = match.group(1)
    prefix = match.group(2)

    bucket = storage_client.get_bucket(bucket_name)  # ?

    # List objects with the given prefix, filtering out folders.
    blob_list = list(bucket.list_blobs(prefix=prefix))
    print('Output files:')
    for blob in blob_list:
        print(blob.name)

    # Process the first output file from GCS.
    # Since we specified batch_size=2, the first response contains
    # the first two pages of the input file.
    output = blob_list[0]

    json_string = output.download_as_string()
    response = json.loads(json_string)

    # The actual response for the first page of the input file.
    first_page_response = response["responses"][0]
    annotation = first_page_response["fullTextAnnotation"]

    print('Full text:\n')
    print(annotation["text"])

    return annotation["text"]


def speech_syntesis(pdf_text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput({"text": pdf_text})

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        {"language_code": 'en-US', "name": "en-US-Neural2-C", "ssml_gender": 'FEMALE'})
    # (       language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig({"audio_encoding": 'MP3'})

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


while True:
    destination_file_name = input("Write the name to save in gcloud: ")
    source_file_name = input("Write the pdf name to read: ")

    if destination_file_name.isalpha() and source_file_name:
        upload_cs_file(destination_file_name, source_file_name)
        pdf_text = async_detect_document(destination_file_name)
        speech_syntesis(pdf_text)

    break
