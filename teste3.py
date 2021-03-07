import streamlit as st
from streamlit_folium import folium_static
import folium
from folium import IFrame
import pandas as pd

import random
import streamlit as st
from streamlit_folium import folium_static
import folium

def random_html_color():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    return '#%02x%02x%02x' % (r, g, b)

def style_fcn(x):
    return { 'fillColor': random_html_color() }
st.image('spectra3.jpg')


mapboxAccessToken = 'pk.eyJ1IjoicGNqZ2VvMiIsImEiOiJja2x3dnBta3AzNGh6MndwbTk5bnBtaWYwIn0.uz6reBxisN3YYfgJuCr8qg'

mapboxTilesetId = 'mapbox.satellite'

df = pd.read_csv("V01_ALEX01_survey_day02b.csv")
df2= df[["nome","estaca","Prof Max 2m p Cravacao","SPT Max ate 2m","Rocha dura ate 5m"]]
x = df['xgeo']
y = df['ygeo']
estaca = df['estaca']
verm=df["Prof Max 2m p Cravacao"]
if st.checkbox('Show dataframe'):
    st.write(df2)
m = folium.Map(location=[-5.268005,-37.967937], zoom_start=15, tiles='https://api.tiles.mapbox.com/v4/' + mapboxTilesetId + '/{z}/{x}/{y}.png?access_token=' + mapboxAccessToken,attr='mapbox.com')
folium.GeoJson("geojson.geojson", style_function=style_fcn).add_to(m)
tooltip = "Liberty Bell"

for i in range(len(x)):
    if (len(verm[i].split())!=2 ):
       picpath=str(estaca[i])+"_figure.png"
       p1='<img src="' + picpath +'" alt="picture" width="400" height="300" align="left" />'
       folium.Marker([y[i], x[i]],icon=folium.Icon(color="blue"), popup=p1, tooltip=str(estaca[i])).add_to(m)
    if (len(verm[i].split())==2 ):
       picpath=str(estaca[i])+"_figure.png"
       p1='<img src="' + picpath +'" alt="picture" width="400" height="300" align="left" />'
       folium.Marker([y[i], x[i]],icon=folium.Icon(color="red"), popup=p1, tooltip=str(estaca[i])).add_to(m)
folium_static(m)