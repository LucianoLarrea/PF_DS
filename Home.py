import pandas as pd
import streamlit as st
from PIL import Image
import plotly.graph_objs as go
import plotly.express as px

options = ['Inicio','Objetivos','Mercado','Regulación','Hitos']
query = st.sidebar.radio('Sección',options)

if query == options[0]:
    image = Image.open('pages/DGRL.png')
    st.image(image, caption='Transforming data into knowledge')
    st.write('Equipo de trabajo')

    st.write('Franco Myburg DATA ENGINEER')
    st.write('Ivanna Villa DATA ANALYST')
    st.write('Jaime Ospino DATA ENGINEER')
    st.write('Luciano Larrea DATA SCIENTIST')
    st.write('Roy Quilca DATA ENGINEER')

if query == options[1]:
    st.subheader('Objetivos')
    st.write('Este trabajo se propone responder las siguientes preguntas:')
    st.write('¿Cuáles son las dimensiones del mercado?			Cuota del mercado')
    st.write('¿Cuáles son las perspectivas del mercado?			Tendencias')
    st.write('¿Cuáles son las zonas con mayor demanda?		Métricas')
    st.write('¿Cuáles son los ingresos proyectados?				KPIs')
    st.write('¿Cuál es el impacto ambiental positivo proyectado?		Calculadora')

if query == options[2]:
    st.subheader('Mercado')
    menu_items = ["Nueva York", "Transporte", "Mercado"]
    menu_selection = st.sidebar.radio("Secciones", menu_items)
    if menu_selection == menu_items[0]:
        st.write('Nueva York')
    if menu_selection == menu_items[1]:
        st.write('Transporte')
    if menu_selection == menu_items[2]:
        st.write('Mercado')
        
if query == options[3]:
    st.subheader('Regulacion')

if query == options[4]:
    st.subheader('Hitos')
    import streamlit as st
    import datetime

    # Definir las fechas de inicio y fin
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2024, 12, 1)

    # Crear una lista con el primer día de cada mes
    months = []
    current_date = start_date
    while current_date <= end_date:
        months.append(current_date)
        current_date = datetime.date(current_date.year + (current_date.month // 12), ((current_date.month % 12) + 1), 1)

    # Convertir la lista en una lista de tuplas con el primer día de cada mes
    month_tuples = [(month, month.strftime('%b %Y')) for month in months]

    # Configurar el slider de fechas utilizando las tuplas
    date_range = st.slider("Selecciona un rango de fechas:",
                        value=(start_date, end_date),
                        min_value=start_date,
                        max_value=end_date,
                        format="MMM YYYY",
                        # step=months,
                        key="date_range")
                        # slider_format="custom",
                        # options=month_tuples)

    # Mostrar el rango de fechas seleccionado
    st.write("Rango de fechas seleccionado:", date_range[0].strftime('%Y-%m'), "a", date_range[1].strftime('%Y-%m'))
