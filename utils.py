import io
import numpy as np
from PIL import Image

import albumentations
import albumentations.pytorch
import torch
import streamlit as st
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials

def transform_image(image_bytes: bytes) -> torch.Tensor:
    transform = albumentations.Compose([
            albumentations.Resize(height=512, width=384),
            albumentations.Normalize(mean=(0.5, 0.5, 0.5),
                                     std=(0.2, 0.2, 0.2)),
            albumentations.pytorch.transforms.ToTensorV2()
        ])
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('RGB')
    image_array = np.array(image)
    return transform(image=image_array)['image'].unsqueeze(0)

def image_to_byte_array(image:Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='png')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

def send_to_bucket(image_name, image_bytes):

    credentials_dict = {
        'type': 'service_account',
        'client_id': st.secrets['gcp']['client_id'],
        'client_email': st.secrets['gcp']['client_email'],
        'private_key_id': st.secrets['gcp']['private_key_id'],
        'private_key': st.secrets['gcp']['private_key'],
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project=st.secrets['gcp']['project_id'])
    bucket = client.get_bucket(st.secrets['gcp']['bucket'])
    bucket.blob(image_name).upload_from_string(image_bytes)
    image_url = bucket.blob(image_name).public_url
    return image_url