#Import Library
import folium
import pandas as pd

#Load Data
data = pd.read_excel("tesla-supercharger-france.xlsx")
latitude = data['Ylatitude']
longitude = data['Xlongitude']
station = data['ad_station']

#Create base map
map = folium.Map(location=[48.754865,2.373034], zoom_start = 6)

#Plot Marker
for latitude, longitude, station in zip(latitude, longitude, station):
    folium.Marker(location=[latitude, longitude], popup=str(station), icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map.html")
