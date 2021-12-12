import streamlit as st
from webcam import webcam
import yaml

import uuid


from predict import load_model, get_prediction
from utils import image_to_byte_array, send_to_bucket




from db import insert_data, get_data


st.sidebar.title("Collected Image")

placeholder = st.sidebar.empty()
st.title("Mask Classification Model")
username = st.text_input('User Name')


def set_images(placeholder, username):
    placeholder.empty()
    pictures = get_data(username)
    with placeholder.container():
        for picture in pictures:
            text = "- Time:{}\n- Name:{}\n- Label:{}".format(str(picture['created_at']), picture['username'], picture['label'])
            st.text(text)
            st.image(picture['image_url'])

def main():
    if username:
        st.write('The current user is', username)
        set_images(placeholder, username)
        

    captured_image = webcam()
    if captured_image is None:
        st.write("Waiting for capture...")
    else:
        st.write("Got an image from the webcam:")
        st.image(captured_image)
        print(captured_image)
        with open("config.yaml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        

        model = load_model()
        model.eval()

        

        if captured_image:

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
    main()


