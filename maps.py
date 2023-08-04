import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns

def final_project():
    st.markdown("Pickup Points")
    image = Image.open('plots/map1.png')
    st.image(image)
    st.markdown("Dropoff Points")
    image = Image.open('plots/map2.png')
    st.image(image)