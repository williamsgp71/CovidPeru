import streamlit as st
import pandas as pd
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_Training = st.beta_container()

with header:
    st.title('Welcome a my awesome data science project')
    st.text('In this project ')
with dataset:
    st.header('NYC taxi dataset')
    st.text('I found this dataset in wwwwwwwwwww......')
    taxi_data = pd.read_csv('D:/EspacioJupyter/datos/taxi_data.csv')
    st.write(taxi_data.head())
with features:
    st.header('The features I created')


with model_Training:
    st.header('Time to train the model')
    st.text('This model do it this')
