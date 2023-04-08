#!activate ai-azure-c1

import sys

sys.path.append("/opt/conda/envs/ai-azure-c1/lib/python3.8/site-packages")

import datetime
import pandas as pd
from PIL import Image
import requests
import io
import glob, os, sys, time, uuid

from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

endpoint = "https://udacity-boarding-kiosk-form-recoginizer.cognitiveservices.azure.com/"
key = "cee697404650442da3886e5b68a27c79"

form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))
print(form_recognizer_client)

content_url = "https://raw.githubusercontent.com/t-drogge/udacity-cd0461-passenger-boarding-kiosk/main/submission/material_preparation_step/id-drogge.png"

id_card_content = form_recognizer_client.begin_recognize_identity_documents_from_url(content_url)

id_card_result = id_card_content.result()

print (id_card_result)