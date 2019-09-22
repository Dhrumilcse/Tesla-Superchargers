#Import Library
import folium
import pandas as pd

#Load Data
data = pd.read_excel("tesla-supercharger-france.xlsx")
latitude = data['Ylatitude']
longitude = data['Xlongitude']
station = data['ad_station']

#Create base map
map = folium.Map(location=[48.754865,2.373034], zoom_start = 6, tiles = "cartodbpositron")

#Plot Marker with custom Icon
for latitude, longitude, station in zip(latitude, longitude, station):
    icon_path = "tesla-iconn.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(30,30))
    folium.Marker(location=[latitude, longitude], popup=str(station), icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map.html")
