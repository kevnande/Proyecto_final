
import streamlit as st
import pandas as pd

# Función para cargar el DataFrame (puedes reemplazarlo con datos reales)
@st.cache
def load_data():
    # DataFrame de ejemplo; reemplázalo con tus datos reales
    data = {
        "Title": ["Film A", "Film B", "Film C", "Film D"],
        "Genre": ["Action", "Drama", "Comedy", "Thriller"],
        "Year": [2021, 2020, 2019, 2018],
        "Rating": [8.5, 7.0, 6.5, 9.0]
    }
    df = pd.DataFrame(data)
    return df

# Cargar los datos
df = load_data()

# Configurar el título del dashboard
st.title("Dashboard de Filmes 🎥")

# Sidebar: Checkbox para visualizar todos los filmes
show_films = st.sidebar.checkbox("Mostrar todos los filmes", value=True)

# Sidebar: Header adicional
st.sidebar.header("Opciones del Dashboard")

# Mostrar los datos si el checkbox está activado
if show_films:
    st.header("Lista de Filmes")
    st.dataframe(df)
else:
    st.info("Selecciona el checkbox para mostrar la lista de filmes.")
