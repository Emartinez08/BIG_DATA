import streamlit as st
import pandas as pd

st.title('App de Bicicletas')

DATA_URL = '/home/kike/Documents/BIG_DATA/csv/citibike-tripdata.csv'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # Convertimos la columna 'started_at' a formato datetime
    data['started_at'] = pd.to_datetime(data['started_at'])
    return data

data_load_state = st.text('Cargando datos...')
data = load_data(1000)
data_load_state.text("¡Datos cargados!")

# Sección de interacción: Filtro por fecha
st.sidebar.header("Filtrar por fecha")
min_date = data['started_at'].min().date()
max_date = data['started_at'].max().date()

# Permite seleccionar un rango de fechas en la barra lateral
selected_dates = st.sidebar.date_input("Selecciona el rango de fechas", (min_date, max_date))

# Filtrar los datos según el rango seleccionado
if isinstance(selected_dates, tuple) or isinstance(selected_dates, list):
    start_date, end_date = selected_dates
    filtered_data = data[(data['started_at'].dt.date >= start_date) & (data['started_at'].dt.date <= end_date)]
else:
    # En caso de que solo se seleccione una fecha
    filtered_data = data[data['started_at'].dt.date == selected_dates]

st.subheader("Datos filtrados por fecha")
st.write(filtered_data)

# Mostrar algunas estadísticas simples
st.subheader("Estadísticas")
total_viajes = filtered_data.shape[0]
st.write("Total de viajes en el rango seleccionado:", total_viajes)
