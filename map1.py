import folium
import webbrowser
from numpy import fill_diagonal
import pandas as pd

data = pd.read_csv("/home/olo/Documents/GitHub/WebMap/Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


m = folium.Map(location=[38.58, -99.09],
               zoom_start=6, tiles="cartodb positron")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(
        el)+" m", fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())

m.save("Map1.html")
webbrowser.open("/home/olo/Documents/GitHub/WebMap/Map1.html")
