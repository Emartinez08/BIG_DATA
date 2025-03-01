#leer el archivo /home/kike/Documents/BIG_DATA/csv/movies.csv

import pandas as pd
import streamlit as st

# Open and read the CSV file
file_path = '/home/kike/Documents/BIG_DATA/csv/movies.csv'
movie_data = pd.read_csv(file_path)


# Display the first few rows of the dataframe
print(movie_data.head())

# Set the title of the Streamlit app
st.title('Nextflix movies')

# Display the dataframe in the Streamlit app
st.dataframe(movie_data)

