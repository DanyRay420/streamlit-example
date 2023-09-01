from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit as st
from PIL import Image
from ultralytics import YOLO

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


@st.cache(allow_output_mutation=True)
def detect_objects(image):
    results = model(image)
    return results.render()  # or any other way you want to process the results

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Detecting objects...")
    detected_image = detect_objects(image)
    st.image(detected_image, caption="Detected Objects", use_column_width=True)


    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
