import pandas as pd
import plotly.express as px
import streamlit as st

# Crear un DataFrame básico con pandas
data = {"Nombre": ["Ana", "Luis", "Carlos"], "Edad": [25, 30, 35]}
df = pd.DataFrame(data)

# Crear un gráfico simple con Plotly Express
fig = px.bar(df, x="Nombre", y="Edad", title="Edades de las personas")

# Mostrar en la terminal
print("DataFrame creado:")
print(df)

# Usar Streamlit (se verá en el navegador)
st.title("Ejemplo con Streamlit")
st.write("Aquí está tu gráfico:")
st.plotly_chart(fig)
