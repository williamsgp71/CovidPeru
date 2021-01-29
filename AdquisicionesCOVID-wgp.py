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

'''Empresas que vendieron productos al Peru'''
empresas = adquisiciones['PROVEEDOR'].unique().tolist()

if st.checkbox('EMPRESAS'):
    st.write(empresas)

option = st.selectbox(
    'pensando por ahora',
     adquisiciones['PROVEEDOR'].unique())
'You selected: ', option

'Cantidad de empresas: ',len(empresas)
'Cantidad minima de un producto: ',adquisiciones['CANTIDAD'].min()
st.write(adquisiciones.loc[adquisiciones['CANTIDAD']==adquisiciones.CANTIDAD.min()] )
'Cantidad maxima de un producto: ',adquisiciones['CANTIDAD'].max()
st.write(adquisiciones.loc[adquisiciones['CANTIDAD']==adquisiciones.CANTIDAD.max()]
)
'Productos que vende el proveedor con la mayor cantidad de productos vendidos'
st.write(adquisiciones.loc[adquisiciones['PROVEEDOR']=='DISTRIBUIDORA DROGUERIA SAGITARIO S.R.L.'])

'Tipo de productos que las empresas le vendieron al Peru'
st.write(adquisiciones['PRODUCTO'].unique())

'Cantidades de productos'
st.write(adquisiciones.groupby('PRODUCTO').aggregate({'CANTIDAD':sum}))

'Productos que mas se vendieron'
st.write(adquisiciones.groupby('PRODUCTO').aggregate({'CANTIDAD':sum})\
.sort_values('CANTIDAD',ascending=False))
