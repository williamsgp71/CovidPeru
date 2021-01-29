import streamlit as st
import pandas as pd

st.title('Analisis de la data de la adquisiciones del COVID-PERU')
st.text('Adquisiciones del Covid Peru')
adquisiciones = pd.read_excel(io='D:/EspacioJupyter/datos/ADQUISISIONES.xls',sheet_name='itemTablaAdquisiciones')
adquisiciones

st.text('Empresas que han vendido mas productos')
emp = adquisiciones.pivot_table(values = 'CANTIDAD',index = ['PROVEEDOR'],
                                aggfunc ='sum')
st.text('Empresas')
st.write(emp['CANTIDAD'].sort_values(ascending =False))

'''Empresas que le vendieron productos al Peru'''
empresas = adquisiciones['PROVEEDOR'].unique().tolist()

if st.checkbox('EMPRESAS'):
    st.write(empresas)
