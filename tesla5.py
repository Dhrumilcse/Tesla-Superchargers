#1.0 Import Library
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#Load Data
data = pd.read_excel("tesla-supercharger-france.xlsx")
lat = data['Ylatitude']
lon = data['Xlongitude']
station = data['n_station']

#Create base map
map = folium.Map(location=[47.85183, 3.542802], zoom_start = 6, tiles = "cartodbpositron" )
#marker_cluster = MarkerCluster().add_to(map)

#Plot Marker
for lat, lon, station in zip(lat, lon, station):
    #Using Custom Tesla Icon
    icon_path = "tesla-iconn.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(30,30))
    folium.Marker(location=[lat, lon], popup=str(station), icon = icon).add_to(map)

#Save the map
map.save("map.html")
