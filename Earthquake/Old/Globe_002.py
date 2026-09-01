import json
import folium

with open('.\Earthquake.json') as json_file:
    data = json.load(json_file)
    for p in data['properties']:
        print("Mag=" + p["mag"])
        print("Place=" + p["place"])
        print("Time=" + p["time"])


m = folium.Map(location=[0, 0], zoom_start=2.5)
folium.Circle(
    radius=100000,
    location=[0, 0],
    popup="The Waterfront",
    color="blue",
    fill=False,
).add_to(m)

m.save(".\Index.html")





# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson