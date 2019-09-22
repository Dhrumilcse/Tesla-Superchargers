#Import Library
import folium

#Create base map
map = folium.Map(location=[48.754865,2.373034], zoom_start = 10)

#Add Marker
folium.Marker(location=[48.754865,2.373034,], popup = "Tesla Supercharger Thiais", icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map.html")
