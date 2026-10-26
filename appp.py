import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from keras.models import load_model

model = load_model("emotion_model.keras")

classes = ['angry', 'disgust', 'fear', 'happy',
           'neutral', 'sad', 'surprise']

st.title("Emotion Recognition")

photo = st.camera_input("Take a photo")

uploaded = st.file_uploader("Or upload an image",type=['jpg', 'jpeg', 'png'])

if photo is not None:
    image = Image.open(photo)

elif uploaded is not None:
    image = Image.open(uploaded)

else:
    image = None

if image is not None:

    st.image(image, width=250)

    image = image.convert('L')
    image = image.resize((48, 48))

    X = np.array(image).reshape(1, 48, 48, 1)

    prediction = model.predict(X, verbose=0)[0]

    emotion = classes[np.argmax(prediction)]

    st.write("Predicted Emotion:", emotion)

    results = pd.DataFrame({'Emotion': classes,'Probability': prediction})

    st.write(results)