import streamlit as st
import pandas as pd

st.title('Netflix app')

DATE_COLUMN = 'released'
DATA_URL = 'https://github.com/Emartinez08/BIG_DATA/blob/main/csv/movies.csv'

@st.cache_data
def load_data(nrows):
    with open(DATA_URL, 'r', encoding='latin1') as doc:
        data = pd.read_csv(doc, nrows=nrows)
    return data

def filter_data_by_filme(data, filme):
    # Se filtran los filmes que contengan el texto buscado (sin distinción entre mayúsculas/minúsculas)
    filtered_data_filme = data[data['name'].str.upper().str.contains(filme)]
    return filtered_data_filme

def filter_data_by_director(data, director):
    filtered_data_director = data[data['director'] == director]
    return filtered_data_director

data_load_state = st.text('Cargando datos...')
data = load_data(1000)
data_load_state.text("¡Datos cargados! (usando st.cache)")

if st.sidebar.checkbox('Mostrar todos los filmes'):
    st.subheader('Todos los filmes')
    st.write(data)

titulofilme = st.sidebar.text_input('Titulo del filme:')
btnBuscar = st.sidebar.button('Buscar filmes')

if btnBuscar:
    data_filme = filter_data_by_filme(data, titulofilme.upper())
    count_row = data_filme.shape[0]  # Número de filas
    st.write(f"Total filmes mostrados: {count_row}")
    st.write(data_filme)

selected_director = st.sidebar.selectbox("Seleccionar Director", data['director'].unique())
btnFilterbyDirector = st.sidebar.button('Filtrar director')

if btnFilterbyDirector:
    filterbydir = filter_data_by_director(data, selected_director)
    count_row = filterbydir.shape[0]  # Número de filas
    st.write(f"Total filmes: {count_row}")
    st.dataframe(filterbydir)
