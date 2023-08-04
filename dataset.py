import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
def final_project():
    st.markdown("Original Dataset")
    image = Image.open('plots/dataframe_head.png')
    st.image(image)
    st.markdown("Tranformed Dataset")
    image = Image.open('plots/trans-4.png')
    st.image(image)

