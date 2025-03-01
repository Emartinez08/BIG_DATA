import pandas as pd
import streamlit as st
import pydeck as pdk

# Open and read the CSV file
file_path = '/home/kike/Documents/bigdata/csv/uber_dataset.csv'
uber_data = pd.read_csv(file_path)

# Rename columns to match the required names
uber_data.rename(columns={'Lat': 'lat', 'Lon': 'lon'}, inplace=True)

# Display the first few rows of the dataframe
print(uber_data.head())

# Set the title of the Streamlit app
st.title('Uber Pickups in New York City')

# Display the dataframe in the Streamlit app
st.dataframe(uber_data)

# Create a map centered around New York City
st.map(uber_data[['lat', 'lon']])

# Define a layer to display on a map
layer = pdk.Layer(
    'ScatterplotLayer',
    data=uber_data,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)

# Set the viewport location
view_state = pdk.ViewState(
    latitude=uber_data['lat'].mean(),
    longitude=uber_data['lon'].mean(),
    zoom=10,
    pitch=50,
)

# Render the deck.gl map in the Streamlit app
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))