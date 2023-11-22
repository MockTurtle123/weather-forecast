import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days:', min_value=1, max_value=5,
                   help='Select the number of days to forecast')
option = st.selectbox('Select data to view',
                      options=('Temperature', 'Sky'))

image_dict = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
              'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}

if place:
    day_s = "day" if days == 1 else "days"
    st.subheader(f'{option} for the next {days} {day_s} in {place.title()}')

    try:
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            temperatures = [i['main']['temp'] for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': "Date", 'y': 'Temperature (C)'})
            st.plotly_chart(figure)
        elif option == 'Sky':
            sky_cond = [i['weather'][0]['main'] for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            image_list = [image_dict[i] for i in sky_cond]
            st.image(image_list, width=150, caption=dates)

    except KeyError:
        st.info(f"Place '{place}' isn't recognised.")

