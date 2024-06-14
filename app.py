import streamlit as st
#st.write('Kabishraghav')
#st.image('image.jpg')
import pandas as pd
import json
import numpy as np
import requests


st.title('Weather Dashboard')
st.subheader('Bahrain')
st.image(f"https://flagcdn.com/80x60/{'bh'}.png")
st.image('bahrain.jpg',width=200)
resp =requests.get('https://api.open-meteo.com/v1/forecast?latitude=26.0333&longitude=50.55&current=temperature_2m,is_day,precipitation,rain,showers,wind_speed_10m,wind_direction_10m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,uv_index_clear_sky_max,precipitation_hours&timezone=GMT')
value = resp.json()
st.sidebar.write('latitude',value['latitude'])
st.sidebar.write('longitude',value['longitude'])
data_type = st.sidebar.selectbox('select the data you need to predict',('temperature','uv index','precipitation','sunrise','sunset'))
temp=value['current']['temperature_2m']
day=value['current']['is_day']
wind=value['current']['wind_speed_10m']
def day_or_night():
    if day == 1:
       st.metric('Day or Night', "Day")
    else:
        st.metric('Day or Night', "Night")
col1,col2,col3= st.columns(3)
with col1:
    st.metric('temperature',temp)
with col2:
    st.metric('wind speed',wind)
with col3:
    day_or_night() 

daily_max_temp_df = pd.DataFrame(value["daily"]["temperature_2m_max"],
                                 value["daily"]["time"])
daily_uv = pd.DataFrame(value["daily"]["uv_index_max"],
                      value['daily']['time'])
daily_sunrise = pd.DataFrame(value['daily']['sunrise'],
                             value['daily']['time'])
daily_precipitation = pd.DataFrame(value['daily']['precipitation_hours'],
                                   value['daily']['time'])
daily_sunset = pd.DataFrame(value['daily']['sunset'],
                            value['daily']['time'])

if data_type == 'temperature':
    st.line_chart(daily_max_temp_df)
elif data_type == 'uv index':
    st.line_chart(daily_uv)
elif data_type =='precipitation':
    st.line_chart(daily_precipitation)
elif data_type == 'sunrise':
    st.line_chart(daily_sunrise)
else:
    st.line_chart(daily_sunset)

st.video('https://youtu.be/nNmWAo0kDGk')



