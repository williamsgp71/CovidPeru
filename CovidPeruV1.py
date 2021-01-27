import streamlit as st
import numpy as np
import pandas as pd
st.title('Analisis de la data del COVID-PERU')

data_covid = pd.read_csv('D:/EspacioJupyter/datos/positivos_covid.csv',sep=';')
st.write(data_covid.head())

st.text('Edad Promedio Por sexo Provincia y departamento')
st.write(data_covid.groupby(['DEPARTAMENTO','PROVINCIA','SEXO']).aggregate({'EDAD':'mean'}).head(50))

st.text('Creamos un dataframe de solo el departamento de Lima')
data_covid_lima = data_covid.loc[data_covid['DEPARTAMENTO']=='LIMA']
st.write(data_covid_lima.head(100))

data_covid_lima2 = data_covid_lima.copy()
data_covid_lima2['RESULTADO'] = 'POSITIVO'
st.text('Numero de personas contagiadas por SEXO Y DISTRITO')
st.write(data_covid_lima2.groupby(['DISTRITO','SEXO']).aggregate({'EDAD':'mean','RESULTADO':'size'})
)


st.text('Promedio de edades y cantidad de personas infectadas por coronavirus')
st.write(data_covid_lima2.groupby('SEXO').aggregate({'EDAD':'mean','RESULTADO':'size'}))

st.text('Estadisticas del dataset covidPeru')
st.write(data_covid_lima.describe())
