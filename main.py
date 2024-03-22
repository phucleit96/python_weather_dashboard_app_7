# Import necessary libraries and functions
import streamlit as st
import plotly.express as px
from backend import get_data

# Set the title of the web application
st.title('Weather Forecast for the Next Days')

# Create a text input field for the user to enter a place
place = st.text_input("Place: ")

# Create a slider for the user to select the number of forecast days
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

# Create a select box for the user to choose between viewing temperature or sky conditions
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Display a subheader that shows the user's current selections
st.subheader(f"{option} for the next {days} days in {place}")

# If a place has been entered, the script tries to get the weather data for that place
if place:
    try:
        filtered_data = get_data(place, days)
    except KeyError:
        # If the place does not exist in the data (causing a KeyError), the script informs the user that the city is not found
        st.info(f"There is no city named as {place}. Please try again!")
    else:
        # If the data is successfully retrieved, the script checks the user's option selection
        if option == "Temperature":
            # If the user selected "Temperature", the script extracts temperature data, converts it from Kelvin to Celsius, and plots it on a line chart
            temperatures = [float(dict['main']['temp']) - 273.15 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            # If the user selected "Sky", the script extracts the sky conditions, maps them to corresponding images, and displays these images
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=115)