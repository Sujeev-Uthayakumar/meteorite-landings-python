import folium
import pandas
from functions import *

df = pandas.read_csv("meteorite-landings.csv")
size = 45716
fg = folium.FeatureGroup(name="Meteorite Landings (> 1 Tonne) Layer")

# Meteorite Landings (> 1 Tonne) Layer
for i in range(1,size):
    if pandas.isnull(df.reclat[i]) or df.mass[i] < 907185:
        print("None output:", i, df.mass[i])
    else:
        markup = "Name: {0}, Date: {1}".format(df.name[i], df.year[i])
        fg.add_child(folium.CircleMarker(location=[df.reclat[i], df.reclong[i]], radius=6,popup=markup, fill_color=colorWeight(df.mass[i]), color='black', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population Layer")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map = folium.Map(location=[8.78,34.5], zoom_start=3, tiles="OpenStreetMap")

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Large Meteorite Landings.html")

