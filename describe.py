import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
import webbrowser
url='https://public.tableau.com/views/Sucharitha_Tableau/HR?:language=en-GB&:display_count=n&:origin=viz_share_link'

def final_project():
    st.markdown("Dataset Description")
    image = Image.open('plots/describe-1.png')
    st.image(image)
    st.markdown(url,unsafe_allow_html=True)
