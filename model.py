import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def final_project():
    pickle_in = open("xgboost_haversine_model.pkl","rb")
    classifier=pickle.load(pickle_in)
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fare Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    passenger_count = st.text_input("Passenger Count","")
    year = st.text_input("year","")
    month= st.text_input("month","")
    distance = st.text_input("Distance","")
    final_result=""
    if st.button("Predict"):
        input=np.array([[passenger_count,year,month,distance]]).astype(np.float64)
        final_result=classifier.predict(input)
        st.success('The output is {}'.format(final_result))
        
        


