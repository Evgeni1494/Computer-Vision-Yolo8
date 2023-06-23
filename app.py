import streamlit as st
from PIL import Image
import cv2
import numpy as np
import torch
from ultralytics import YOLO
from matplotlib import pyplot as plt

def load_model():
    model = YOLO('best.torchscript')
    
    return model

def predict(image, model):
    res = model(image)
    res_plotted = res[0].plot()
    image_with_boxes = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
    return image_with_boxes


def main():
    st.title('Smoke Detection with YOLO')
    model = load_model()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Predicting...")

        result_img = predict(image,model)
        st.image(result_img, caption='Output Image with Bounding Boxes', use_column_width=True)


if __name__ == "__main__":
    main()
