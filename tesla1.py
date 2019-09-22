#Import Library
import folium

#Create base map
map = folium.Map(location=[48.8566, 2.3522], zoom_start = 10)

#Save the map
map.save("map.html")
