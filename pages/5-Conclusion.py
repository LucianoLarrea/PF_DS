import pandas as pd
import streamlit as st
import utils.paths as path
import base64
from io import BytesIO
# Ruta del directorio que contiene el archivo
data_dir = path.make_dir_function(['app','data']) #'roy',
# Lectura del PDF como un objeto binario
with open(data_dir("Informe_Final.pdf"), "rb") as f:
    archivo_pdf = f.read()
# Transformando el pdf a 
def codificar_base64(archivo):
    with open(archivo, "rb") as f:
        datos = f.read()
        base64_pdf = base64.b64encode(datos).decode('utf-8')
    return base64_pdf

st.markdown("""
            <style>
            .btn-download-pdf {
                display: flex;
                flex-direction: column;
                align-content: center;
                text-align: center;
                width: 210px;
            }
            .btn-download-pdf a{
                text-decoration: none;
            }
            </style>
            """, unsafe_allow_html=True)
# Boton de descarga
descarga = st.button('Generate Analysis Report in Spanish', type='primary')
if descarga:
    b64 = codificar_base64(data_dir('Informe_Final.pdf'))
    href = f"""
    <p class="btn-download-pdf" align="center">
        <a href="data:application/octet-stream;base64,{b64}" download="Informe_Final.pdf">Download PDF</a>
    </p>"""
    st.markdown(href, unsafe_allow_html=True)

st.title('Summary')
# st.markdown('[Spanish Final Report](https://drive.google.com/file/d/1qEj5GNK7Wj63LplsRg7F-1ClpW_enPXz/view?usp=share_link)', unsafe_allow_html=True)
st.header('The State of the Taxi Industry')
st.subheader('Taxi Trip Counts and Locations')
st.write('Monthly Taxi trip counts steadily decreased more than 80% since 2013 to 2023')
st.write('Total trips per vehicle decreased more than 75% since 2013 to 2023')
st.write('Trip locations for Taxis have remained fairly constant, centralized in Manhattan and at JFK and LaGuardia airport')
st.subheader('Driver Statistics')
st.write('The number of “active” Taxi Vehicles decreased 43% since 2013 to 2023')
st.write('The number of “active” Taxi Drivers decreased 68% since 2013 to 2023')
st.write('The ratio of Drivers/Vehicles decreased from 2,5 in 2013 to 1,4 in 2023')
st.subheader('Gross Income')
st.write('The average Farebox per Day decreased 65% since 2013 to 2023')
st.write('The average Farebox per Vehicle decreased 50% since 2013 to 2023')
st.header('Forecasting of the Taxi Industry')
st.write('The number of vehicles is projected to peak at 9,500 total taxis by April 2024 and then begin to decline again')
st.write('By the end of 2025, 8,770 vehicles are projected, 1,000 more than january 2023')
st.write('If the downward trend continues, it could reach a minimum by August 2024, this date being the most critical point for the taxi industry')
st.header('Recommendations')
st.write('While investing in a bear market is extremely risky, it also represents an opportunity for those who wish to strongly position themselves in the market')
st.write('Those who manage to survive the looming crisis in the yellow taxi industry and manage to position themselves as leaders in service, sustainability and innovation will be the ones who dominate the future of the market.')

