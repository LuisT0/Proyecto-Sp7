import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('🚗 Car insights: Explora los anuncios vehiculares') #Encabezado principal
st.subheader('Una breve descripción de la estadística detrás de los vehículos anunciados')

st.header('Gráficos para comparar precio y kilometraje')      
#Escribimos 2 checkbox para darle al usuario 2 opciones para visualizar los gráficos
if st.checkbox('Mostrar gráfico dispersión precio vs kilometraje'): #casilla de verificación para el primer gráfico
    st.header('Relación entre el precio y kilometraje')
    fig1 = px.scatter(car_data, x='odometer', y='price', color='condition', title='Precio VS Kilometraje') #Crear el gráfico
    st.plotly_chart(fig1, use_container_width=True) #mostrar el gráfico

#Creamos el segundo checkbox
if st.checkbox('Mostrar gráfico de lineas precio vs kilometraje'):
    st.header('Relación entre el precio y kilometraje')
    fig2 = px.line(car_data, x='odometer', y='price', color='condition', title='Precio VS Kilometraje') #crear el gráfico
    st.plotly_chart(fig2, use_container_width=True) #mostrar el gráfico

st.header('Gráfico para ver la relación del precio y modelo')

#Creamos otro gráfico para mostrar el precio y el modelo
if st.button('Mostrar el gráfico de dispersion precio y modelo'):
    st.header('Relacion entre el precio y el año del modelo')
    fig3 = px.scatter(car_data, x='model_year', y='price', color='condition', title='Precio VS Año Del Modelo')
    st.plotly_chart(fig3, use_container_width=True)

st.header('Gráfico para visualizar el kilometraje de los autos')

#Creamos el boton para el histograma
if st.button('Mostrar el histograma del kilometraje'):
    st.header('Kilometraje de los automóviles')
    fig4 = px.histogram(car_data, x='odometer', nbins=30,
                        title='Distribución del kilometraje de los vehículos',
                        labels={'odometer': 'Kilometraje'},
                        color_discrete_sequence=['orange'])
    fig4.update_layout(bargap=0.2)
    st.plotly_chart(fig4, use_container_width=True)




