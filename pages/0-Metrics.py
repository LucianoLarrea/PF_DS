import pandas as pd
import numpy as np
import streamlit as st
import datetime
import plotly.graph_objs as go
import plotly.express as px
import app.connection.get_data as get_data

# df = pd.read_csv('Proyecto_grupal_DS/luciano/df.csv',index_col=13)
df = pd.read_csv('df.csv',index_col=13)
# Convertir el índice del dataframe en datetime
df.index = pd.to_datetime(df.index)
# df = df[df['license_class']=='Yellow']

# Dashboard layout
# def dashboard_ui():
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")
fleet = st.sidebar.number_input('Fleet Number',1,100000,value=1000)
# monthdate = st.sidebar.date_input("Month Date", datetime.date(2023, 1, 1))
# Obtener la fecha seleccionada en el date_input
# selected_date = pd.to_datetime(monthdate)
# Obtener la fecha seleccionada en el date_input
start_date = datetime.date(2015, 1, 1)  #st.date_input('Start Date',
end_date = datetime.date(2023, 1, 1)    # st.date_input('End Date',
current_date = datetime.date(2023, 1, 1)

selected_date = st.sidebar.slider("Select a date range:",
                    value=(current_date),
                    min_value=start_date,
                    max_value=end_date,
                    format="MMM YYYY",
                    # step = month,
                    key="date_range")
selected_date = selected_date.replace(day=1)
selected_date = pd.to_datetime(selected_date)
selected_date_pos = df.index.get_loc(selected_date)
# Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
unique_vehicles_value = df[df['license_class']=='Yellow'].loc[selected_date, 'unique_vehicles']
market_share = fleet / (fleet + unique_vehicles_value)
market_share_percentage = market_share * 100
# Sidebar menu
# st.sidebar.title("Menu")
menu_items = ["Vehicles", "Trips", "Farebox", "Ratios"]
menu_selection = st.sidebar.radio("Select a page", menu_items)
colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}
df['color'] = df['license_class'].map(colors)

# Dashboard page
if menu_selection == menu_items[0]:
    
    # st.write(f"El valor de unique_vehicles para la fecha seleccionada ({selected_date}) es {unique_vehicles_value}")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Market Vehicles',unique_vehicles_value)
    with col2:
        st.metric('Taxi Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        st.metric('Fleet Vehicles', fleet)
    with col4:
        ev_market_share = 100* fleet / (fleet + unique_vehicles_value/100)
        st.metric('EV Taxi Market Share', f'{ev_market_share:.2f}%')
    
    fig = go.Figure()
    # st.plotly_chart(fig, config=dict(displayModeBar=False), use_container_width=True)
    # fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='unique_vehicles', color='color')
    if  st.checkbox('Show Vehicles FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['unique_vehicles'], mode='lines', name='FHV - High Volume'))
    # fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['unique_vehicles'], mode='lines', name='Yellow'))
    yellow_trace = go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['unique_vehicles'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['unique_vehicles'].idxmax()  
    
    # fig.add_shape(type='line',
    #         x0=proy_Y.index[selected_date_pos],
    #         y0=0,
    #         x1=proy_Y.index[selected_date_pos],
    #         y1=max(df[df['license_class']=='Yellow']['unique_vehicles']),
    #         line=dict(color='red', width=2, dash='dash'))
    # fig.add_shape(
    #         type='line',
    #         x0=proy_Y.index[0],
    #         y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'],
    #         x1=proy_Y.index[-1],
    #         y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'],
    #         line=dict(color='red', width=2, dash='dash'))
    
    fig.add_shape(type="line",
            x0=df.index[selected_date_pos], 
            y0=2000,
            x1=df.index[selected_date_pos], 
            y1=max_y,
            line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
            x0=df.index[0], 
            y0=max_y,
            x1=df.index[-1], 
            y1=max_y,
            line=dict(color='red', dash='dash'))
    
    

    # fig.add_shape(type="line",
    #           x0=df.loc[idx_max_y, 'month_year1'], 
    #           y0=2000,
    #           x1=df.loc[idx_max_y, 'month_year1'], 
    #           y1=max_y,
    #           line=dict(color='red', dash='dash'))
    # fig.add_shape(type="line",
    #           x0=df.loc[idx_max_y, 'month_year1'], 
    #           y0=max_y,
    #           x1=df['month_year1'].iloc[-1], 
    #           y1=max_y,
    #           line=dict(color='red', dash='dash'))
    
    

    
    fig.update_layout(
    title='Unique Vehicles - Max Yellow: '+ str(max_y),
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Unique Vehicles'))
    st.plotly_chart(fig, use_container_width=True)
    
    # df = df[df['license_class']=='Yellow']
    unique_drivers_value = df[df['license_class']=='Yellow'].loc[selected_date, 'unique_drivers']
    st.metric('Market Drivers',unique_drivers_value)
    fig = go.Figure()
    if  st.checkbox('Show Drivers FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['unique_drivers'], mode='lines', name='FHV - High Volume'))
    # fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['unique_drivers'], mode='lines', name='Yellow'))
    yellow_trace=go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['unique_drivers'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['unique_drivers'].idxmax()   #df[df['license_class']=='Yellow']['unique_vehicles']

    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], 
              y0=max_y,
              x1=df['month_year1'].iloc[-1], 
              y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], 
              y0=0,
              x1=df.loc[idx_max_y, 'month_year1'], 
              y1=max_y,
              line=dict(color='red', dash='dash'))



    fig.update_layout(
    title='Unique Drivers - Max Yellow: '+ str(max_y),
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Unique Drivers'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.metric('Market Drivers/Vehicles',round(unique_drivers_value/unique_vehicles_value,1))
    fig = go.Figure()
    if  st.checkbox('Show Drivers/Vehicles FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['drivers_vehicles_ratio'], mode='lines', name='FHV - High Volume'))
    # fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['drivers_vehicles_ratio'], mode='lines', name='Yellow'))
    yellow_trace=go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['drivers_vehicles_ratio'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['drivers_vehicles_ratio'].idxmax()   

    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], 
              y0=max_y,
              x1=df['month_year1'].iloc[-1], 
              y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], 
              y0=1,
              x1=df.loc[idx_max_y, 'month_year1'], 
              y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.update_layout(
    title='Drivers / Vehicles Ratio - Max Yellow: '+ str(round(max_y,1)),
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Drivers / Vehicles Ratio'))
    st.plotly_chart(fig, use_container_width=True)

if menu_selection == menu_items[1]:
    # st.header("Dashboard")
    # st.sidebar.subheader("Choose a Date Range")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        trips_day_value = df[df['license_class']=='Yellow'].loc[selected_date, 'trips_per_day']
        st.metric('Market Trips per day',trips_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_trips = int(trips_day_value * market_share)
        st.metric('Fleet Trips per day',shared_trips)

    # colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}

    # # Create a new column with the corresponding color for each license class
    # df['color'] = df['license_class'].map(colors)
    # Create two line charts with different license classes
    fig = go.Figure()
    if  st.checkbox('Show Trips/Day FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['trips_per_day'], mode='lines', name='FHV - High Volume'))
    # fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['trips_per_day'], mode='lines', name='Yellow'))
    # fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='trips_per_day', color='color')
    # fig2 = px.line(df[df['license_class']=='Green'], x='month_date', y='trips_per_day',color='color')
    # fig3 = px.line(df[df['license_class']=='FHV - High Volume'], x='month_date', y='trips_per_day', color='color')
    # fig4 = px.line(df[df['license_class']=='FHV - Black Car'], x='month_date', y='trips_per_day', color='color')
    # fig5 = px.line(df[df['license_class']=='FHV - Livery'], x='month_date', y='trips_per_day',color='color')
    # fig6 = px.line(df[df['license_class']=='FHV - Lux Limo'], x='month_date', y='trips_per_day', color='color')
    # fig.add_traces(fig2.data + fig3.data + fig4.data + fig5.data + fig6.data)
    yellow_trace = go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['trips_per_day'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['trips_per_day'].idxmax()

    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=max_y,
              x1=df['month_year1'].iloc[-1], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=0,
              x1=df.loc[idx_max_y, 'month_year1'], y1=max_y,
              line=dict(color='red', dash='dash'))


    fig.update_layout(
    title='Trips per Day - Max Yellow: '+ str(max_y),
    xaxis=dict(title='Month & Year', showgrid=True),
    yaxis=dict(title='Trips Per Day'))

    st.plotly_chart(fig, use_container_width=True)  #

    # st.plotly_chart(df['trips_per_day'], use_container_width=True)
    # st.plotly_chart(df['trips_year'], use_container_width=True)
    
    # st.write("### Trips per Month")
    # st.plotly_chart(df['trips_per_month'], use_container_width=True)
    # st.write("### Medallions per Month")
    # st.plotly_chart(df['medallions_per_month'], use_container_width=True)
    
    # st.sidebar.subheader("Monthly")
    # monthlydate = st.sidebar.date_input("Monthly Date", [datetime.date(2016, 1, 1), datetime.date.today()])
    # element_id1_m = st.sidebar.selectbox("Select Your Variable for x-axis", ("month_date", "week", "year"))
    # element_id2_m = st.sidebar.selectbox("Select Your Variable for y-axis", ("trips_per_day", "trips_per_day_shared", "farebox_per_day", "unique_drivers", "unique_vehicles", "avg_minutes_per_trip", "avg_days_vehicles_on_road", "avg_hours_per_day_per_vehicle", "avg_days_drivers_on_road", "avg_hours_per_day_per_driver", "percent_of_trips_paid_with_credit_card"))
    # element_id3_m = st.sidebar.selectbox("Select Your Grouping Variable", ("license_class",))
    
    # st.write("### Outputs")
    # st.write("#### id1_m")
    # st.write("#### id2_m")
    # st.write("#### id3_m")


   # st.plotly

if menu_selection == menu_items[2]:
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        farebox_day_value = df[df['license_class']=='Yellow'].loc[selected_date, 'farebox_per_day']
        st.metric('Market Farebox per day USD',farebox_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_farebox = int(farebox_day_value * market_share)
        st.metric('Fleet Farebox per day USD',shared_farebox)
    # colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}
    # df['color'] = df['license_class'].map(colors)
    # fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='farebox_per_day', color='color')
    fig = go.Figure()
    yellow_trace = go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['farebox_per_day'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['farebox_per_day'].idxmax()   

    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=max_y,
              x1=df['month_year1'].iloc[-1], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=2000,
              x1=df.loc[idx_max_y, 'month_year1'], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.update_layout(
    title='Average Farebox per Day',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Farebox Per Day'))
    st.plotly_chart(fig, use_container_width=True)


    
if menu_selection == menu_items[3]:
    
    col1, col2, col3 = st.columns(3)
    with col1:
        farebox_month_value = df[df['license_class']=='Yellow'].loc[selected_date, 'monthly_farebox_per_vehicle_on_road']
        st.metric('Farebox per month per vehicle USD',int(farebox_month_value))
    with col2:
        farebox_trip_value = df[df['license_class']=='Yellow'].loc[selected_date, 'monthly_farebox_per_trip_on_road']
        st.metric('Farebox per trip',round(farebox_trip_value,1))
    with col3:
        trips_vehicle_value = df[df['license_class']=='Yellow'].loc[selected_date, 'monthly_trips_per_vehicle_on_road']
        st.metric('Trips per vehicle',int(trips_vehicle_value))
    fig = go.Figure()
    # fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_farebox_per_vehicle_on_road', color='color')
    yellow_trace = go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['monthly_farebox_per_vehicle_on_road'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['monthly_farebox_per_vehicle_on_road'].idxmax()   
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=max_y,
              x1=df['month_year1'].iloc[-1], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=0,
              x1=df.loc[idx_max_y, 'month_year1'], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.update_layout(
    title='Monthly Farebox Per Vehicle On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Farebox Per Vehicle On Road'))
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_farebox_per_trip_on_road', color='color')
    fig.update_layout(
    title='Monthly Farebox Per Trip On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Farebox Per Trip On Road'))
    st.plotly_chart(fig, use_container_width=True)
    fig = go.Figure()
    # fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_trips_per_vehicle_on_road', color='color')
    yellow_trace = go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['monthly_trips_per_vehicle_on_road'], mode='lines', name='Yellow')
    fig.add_trace(yellow_trace)
    max_y = max(yellow_trace.y)
    idx_max_y = df[df['license_class']=='Yellow']['monthly_trips_per_vehicle_on_road'].idxmax()   

    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=max_y,
              x1=df['month_year1'].iloc[-1], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.add_shape(type="line",
              x0=df.loc[idx_max_y, 'month_year1'], y0=0,
              x1=df.loc[idx_max_y, 'month_year1'], y1=max_y,
              line=dict(color='red', dash='dash'))
    fig.update_layout(
    title='Monthly Trips Per Vehicle On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Trips Per Vehicle On Road'))
    st.plotly_chart(fig, use_container_width=True)
# start_date = st.sidebar.date_input('Start Date',datetime.date(2013, 1, 1))
# end_date = st.sidebar.date_input('End Date',datetime.date(2023, 1, 1)) 