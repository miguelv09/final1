import streamlit as st
import requests
import pandas as pd
import time

st.title('Monitor de Temperatura y Humedad')

temperature = st.empty()
humidity = st.empty()
chart_data = st.empty()

data_points = []

def get_data():
    response = requests.get('https://wokwi.com/projects/399355596323807233')  
    return response.json()

while True:
    data = get_data()
    temp = data['temperature']
    hum = data['humidity']

    temperature.metric("Temperatura", f"{temp} °C")
    humidity.metric("Humedad", f"{hum} %")

    data_points.append([time.time(), temp, hum])
    df = pd.DataFrame(data_points, columns=['Time', 'Temperature', 'Humidity'])

    chart_data.line_chart(df.set_index('Time'))

    time.sleep(2)
