import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns


def final_project():
    st.markdown("Transformation-1")
    image = Image.open('plots/trans-1.png')
    st.image(image)
    st.markdown("Transformation-2")
    image = Image.open('plots/trans-2.png')
    st.image(image)
    st.markdown("Transformation-3")
    image = Image.open('plots/trans-3.png')
    st.image(image)
    st.markdown("Transformation-4")
    image = Image.open('plots/trans-4.png')
    st.image(image)