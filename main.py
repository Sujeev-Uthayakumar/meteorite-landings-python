import folium
import pandas

df = pandas.read_csv("meteorite-landings.csv")
size = 45716
fg = folium.FeatureGroup(name="My Map")

for i in range(1,size):
    if pandas.isnull(df.reclat[i]) or df.mass[i] < 907185:
        print("Null", i, df.mass[i])
    else:
        fg.add_child(folium.Marker(location=[df.reclat[i], df.reclong[i]], popup=df.name[i], icon=folium.Icon(color='red')))

map = folium.Map(location=[8.78,34.5], zoom_start=3, tiles="OpenStreetMap")

map.add_child(fg)
map.save("Map1.html")

