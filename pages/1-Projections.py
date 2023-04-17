import pandas as pd
import streamlit as st
import datetime
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_csv('Proyecto_grupal_DS/luciano/df.csv')
Ptrips = pd.read_csv('Proyecto_grupal_DS/luciano/ML/proy_Y_trips.csv')
proy_Y = pd.read_csv('Proyecto_grupal_DS/luciano/ML/proy_Y.csv')

# Dashboard layout
# def dashboard_ui():
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")

st.sidebar.title("Menu")
menu = ["Yellow", "Green", "FHVHV"]
menu_selection = st.sidebar.selectbox("Select a license class", menu)

# Sidebar menu
menu_items = ["Trips", "Farebox", "Distances"]
menu_selection = st.sidebar.selectbox("Select a metric", menu_items)


# Dashboard page
if menu_selection == menu_items[0]:
    st.header("Dashboard")
    st.sidebar.subheader("Choose a Date Range")
    monthdate = st.sidebar.date_input("Month Date", [datetime.date(2014, 1, 1), datetime.date(2022, 12, 1)])
    dimension = st.sidebar.selectbox("Choose Metric", ("Trips, Drivers & Vehicles", "Time & Money"))
    colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}

    # Create a new column with the corresponding color for each license class
    df['color'] = df['license_class'].map(colors)
    # Create two line charts with different license classes
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='trips_per_day', color='color')
    fig2 = px.line(Ptrips['trips_per_day'], x=Ptrips.index, y='trips_per_day')
    # fig2 = px.line(df[df['license_class']=='Green'], x='month_date', y='trips_per_day',color='color')
    # fig3 = px.line(df[df['license_class']=='FHV - High Volume'], x='month_date', y='trips_per_day', color='color')
    # fig4 = px.line(df[df['license_class']=='FHV - Black Car'], x='month_date', y='trips_per_day', color='color')
    # fig5 = px.line(df[df['license_class']=='FHV - Livery'], x='month_date', y='trips_per_day',color='color')
    # fig6 = px.line(df[df['license_class']=='FHV - Lux Limo'], x='month_date', y='trips_per_day', color='color')
    fig.add_traces(fig2.data)
    fig.update_layout(
    title='Yellow Taxi: Average Trips per Day each Month',
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

if menu_selection == menu_items[1]:
    # Define main function
    def main():
        
        # Create sidebar for date range selection
        # start_date1, end_date1 = st.sidebar.date_input(
        #     'Select a date range', 
        #     value=(pd.to_datetime('2020-01-01'), pd.to_datetime('2021-12-31')))
        
        # Subset data based on selected date range
        # td = df.query(
        #     'month_date >= @start_date and month_date <= @end_date'
        # )[['trips_per_day', 'month_date', 'license_class']]
        
        # Create Plotly figure
        fig = go.Figure(
            go.Scatter(
                x=df['month_date'], 
                y=df['trips_per_day']))
                # split=df['license_class']
                # mode='lines',
                # line=dict(color=df['license_class'], colorscale='Viridis')))
        
        # Set chart title and axis labels
        fig.update_layout(
            title='Average Trips per Day each Month',
            xaxis=dict(title='Month & Year', showgrid=False),
            yaxis=dict(title='Trips Per Day'))
        
        # Render chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # Run main function
    if __name__ == '__main__':
        main()
        
if menu_selection == menu_items[2]:
    st.write('Air Pollution and Sound Pollution')
    

# start_date = st.sidebar.date_input('Start Date',datetime.date(2013, 1, 1))
# end_date = st.sidebar.date_input('End Date',datetime.date(2023, 1, 1)) 