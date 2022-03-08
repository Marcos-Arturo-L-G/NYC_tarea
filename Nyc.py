
import pandas as pd
import numpy as np
import streamlit as st

st.title('Citybike')
st.subheader('Integrantes: Marcos Arturo Lopez Gonzalez')
st.subheader('Jose Obed Mariano Hipolito')

sidebar = st.sidebar
sidebar.title("Menu")


DATA_URL = ('https://raw.githubusercontent.com/Marcos-Arturo-L-G/NYC_tarea/master/citibike-tripdata.csv')
DATE_COLUMN = 'started_at'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

Mostrar_todo = sidebar.checkbox("Mostrar todos los datos")
if Mostrar_todo:
  data = load_data(2000)
  st.text("Todos los datos:")
  st.dataframe(data)

RecPorHora = sidebar.checkbox("Mostrar los recorridos por hora")
if RecPorHora:
  data = load_data(2000)
  st.subheader('Numero de recorridos por hora')
  hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
  st.bar_chart(hist_values)

hour_tofilter = sidebar.slider('HORA', 0, 23, 9)
if hour_tofilter:
  data = load_data(2000)
  data_rename = data.rename(columns = {'start_lat': 'lat', 'start_lng': 'lon'}, inplace = False)

  filtered_data = data_rename[data_rename[DATE_COLUMN].dt.hour == hour_tofilter]

  st.subheader('Mapa de los recorridos iniciados a las %s:00' % hour_tofilter)
  st.map(filtered_data)