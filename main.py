import streamlit as st
from webcam import webcam
import yaml
import uuid
from predict import load_model, get_prediction
from utils import image_to_byte_array, send_to_bucket
from db import insert_data, get_data


import sentry_sdk
from sentry_sdk import capture_exception

sentry_sdk.init(
    st.secrets['sentry']['sentry_url'],
    traces_sample_rate=1.0
)

def set_images(placeholder, username):
    placeholder.empty()
    pictures = get_data(username)
    with placeholder.container():
        for picture in pictures:
            text = "- Time:{}\n- Name:{}\n- Label:{}".format(str(picture['created_at']), picture['username'], picture['label'])
            st.text(text)
            st.image(picture['image_url'])

def main():
    st.sidebar.title("Collected Image")
    st.title("Mask Classification Model")
    placeholder = st.sidebar.empty()

    username = st.text_input('User Name')
    if username:
        st.write('The current user is', username)
        set_images(placeholder, username)
        

    captured_image = webcam()
    if captured_image is None:
        st.write("Waiting for capture...")
    else:
        st.write("Got an image from the webcam:")
        st.image(captured_image)
        
        with open("config.yaml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        

        model = load_model()
        model.eval()

       
        if not username:
            raise "No username"
        image_bytes = image_to_byte_array(captured_image)
        image_name = uuid.uuid4().hex+".png"
        image_url = send_to_bucket(image_name, image_bytes)

        st.write("Classifying...")
        _, y_hat = get_prediction(model, image_bytes)
        label = ','.join(config['classes'][y_hat.item()])

        st.write(f'label is {label}')
        insert_data(username, image_url, label)
        set_images(placeholder, username)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        capture_exception(e)
        raise e


