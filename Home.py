import pandas as pd
import streamlit as st
from PIL import Image
import plotly.graph_objs as go
import plotly.express as px
from app.connection.get_data import get_data

query2 = 'SELECT * FROM [monthly_report]'
df = get_data(query2)

options = ['Home','Goals','Market']
query = st.sidebar.radio('Sección',options)

if query == options[0]:
    image = Image.open('pages/DGRL.png')
    st.image(image, caption='Transforming data into knowledge')
    st.write('Team')

    st.write('Franco Myburg DATA ENGINEER')
    st.write('Ivanna Villa DATA ANALYST')
    st.write('Jaime Ospino DATA ENGINEER')
    st.write('Luciano Larrea DATA SCIENTIST')
    st.write('Roy Quilca DATA ENGINEER')

if query == options[1]:
    st.subheader('Goals')
    st.write('This work aims to answer the following questions:')
    st.write('¿What are the dimensions of the market?	=>  Market Share')
    st.write('¿What are the market prospects?	=>	Trends')
    st.write('¿What are the areas with the highest demand?	=>	Metrics')
    st.write('¿What are the projected revenues?		=>	KPIs')
    st.write('¿What is the projected positive environmental impact?	=>	Calculator')

if query == options[2]:
    st.subheader('Market')
    # menu_items = ["New York", "Transport", "Market"]
    # menu_selection = st.sidebar.radio("Sections", menu_items)
    # if menu_selection == menu_items[0]:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('New York City')
        image = Image.open('pages/NYC.png')
        st.image(image, caption='Boroughs')
    with col2:
        st.write('Boroughs')
        image = Image.open('pages/NYCTable.png')
        st.image(image, caption='Data')
    # if menu_selection == menu_items[1]:
    #     st.write('Transport')
    # if menu_selection == menu_items[2]:
    #     st.write('Market')
        
# if query == options[3]:
#     st.subheader('Regulacion')

# if query == options[3]:
#     st.subheader('Milestones')
    
    
    
    
    
    
    
    # import streamlit as st
    # import datetime

    # # Definir las fechas de inicio y fin
    # start_date = datetime.date(2010, 1, 1)
    # end_date = datetime.date(2024, 12, 1)

    # # Crear una lista con el primer día de cada mes
    # months = []
    # current_date = start_date
    # while current_date <= end_date:
    #     months.append(current_date)
    #     current_date = datetime.date(current_date.year + (current_date.month // 12), ((current_date.month % 12) + 1), 1)

    # # Convertir la lista en una lista de tuplas con el primer día de cada mes
    # month_tuples = [(month, month.strftime('%b %Y')) for month in months]

    # # Configurar el slider de fechas utilizando las tuplas
    # date_range = st.slider("Selecciona un rango de fechas:",
    #                     value=(start_date, end_date),
    #                     min_value=start_date,
    #                     max_value=end_date,
    #                     format="MMM YYYY",
    #                     # step=months,
    #                     key="date_range")
    #                     # slider_format="custom",
    #                     # options=month_tuples)

    # # Mostrar el rango de fechas seleccionado
    # st.write("Rango de fechas seleccionado:", date_range[0].strftime('%Y-%m'), "a", date_range[1].strftime('%Y-%m'))
