#Import Library
import folium

#Create base map
map = folium.Map(location=[48.754865,2.373034], zoom_start = 10)

#Add Multiple Marker
for coordinates in [[48.754865,2.373034],[49.20858,2.605978]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map.html")
