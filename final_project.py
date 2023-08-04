import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
import dataset
import describe
import transformation
import graphs
import maps
import model




st.markdown("<h1 style='text-align: center; color:  red;'>NYC Fare Prediction App</h1>", unsafe_allow_html=True)
st.title("")

Pages={
        "Dataset"        :  dataset,
        "Description"    :  describe,
        "Transformation" :  transformation,
        "Graphs"         :  graphs,
        "Maps"           :  maps,
        "Model"          :  model
      }

st.sidebar.title('Main Menu')
selection = st.sidebar.radio("Go to", list(Pages.keys()))
page = Pages[selection]
page.final_project()

























    


