#----------------------------------------------------------#
#             Program: Eartquake 2021/04/25                #
#               All rights reserved 2021                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             #
# Mapa global com os terremotos mais recentes              #
#----------------------------------------------------------#

import csv
import folium
import urllib
import webbrowser
import datetime

# Obtem o arquivo de terremotos da internet
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.csv

file = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv")

# Monta a lista de tremores com base no arquivo csv da internet 
wlist = []
for line in file:
    llist = []
    nline = str(line.decode("utf-8")).replace("\n","")
    nline = nline.split(",")
    if nline[0] != "time":
        wlist.append(nline)

file = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv")

# Monta a lista de tremores com base no arquivo csv da internet 
mlist = []
for line in file:
    llist = []
    nline = str(line.decode("utf-8")).replace("\n","")
    nline = nline.split(",")
    if nline[0] != "time":
        mlist.append(nline)

# Inverte a ordem dos tremores mais antigos primeiro 
wlist.reverse()
mlist.reverse()

# Cria o mapa base para os dados
fmap = folium.Map(location=[0, 0], 
                  zoom_start=2.5,
                  tiles="OpenStreetMap")

# Inclui as bordas tectonicas no mapa
def tract_styles(feature):
    return {"fillColor": "green",
            "color": "purple",
            "weight": 1,
            "dashArray": "5, 5",
            "fillOpacity": 1}

folium.GeoJson("https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json",
               name="Tectonics",
               style_function=tract_styles).add_to(fmap)


wGroup = folium.FeatureGroup(name='Magnitude').add_to(fmap)
mGroup = folium.FeatureGroup(name='Earthquakes').add_to(fmap)

nDay = datetime.datetime.utcnow().day

for row in wlist:

    cDate = row[0][0:10]
    cTime = row[0][11:22]
    cDay = int(row[0][8:10])
    cLong = float(row[1].strip())
    cLati = float(row[2].strip())
    cDeep = row[3].strip()
    cMag = float(row[4].strip())
    cRadius = pow(float(cMag),2) # * 10000
    cPlace = row[13].strip()
    cPopup = "Date:" + cDate + "\nTime:" + cTime + "\nMag:" + str(cMag) + "\nDeep:" + cDeep + "Km\nPlace:" + cPlace
    cColor = "yellow"

    if cDay == nDay: 
        cColor = "red"
    if cDay == (nDay - 1): 
        cColor = "orange"

    # Cria o circulo marcando o epicentro do tremor  
    folium.CircleMarker(
        radius=cRadius,
        weight=1,
        popup=cPopup,
        location=[cLong, cLati],
        color=cColor,
        opacity=1,
        fill_color=cColor,
        fill_opacity=0.1,        
        fill=True).add_to(wGroup)

for row in mlist:

    cDate = row[0][0:10]
    cTime = row[0][11:22]
    cDay = int(row[0][8:10])
    cLong = float(row[1].strip())
    cLati = float(row[2].strip())
    cDeep = row[3].strip()
    cMag = float(row[4].strip())
    cRadius = pow(float(cMag),2) # * 10000
    cPlace = row[13].strip()
    cPopup = "Date:" + cDate + "\nTime:" + cTime + "\nMag:" + str(cMag) + "\nDeep:" + cDeep + "Km\nPlace:" + cPlace
    cColor = "yellow"

    if cDay == nDay: 
        cColor = "red"
    if cDay == (nDay - 1): 
        cColor = "orange"

    # Cria o circulo baseado na magnetude do tremor  
    folium.CircleMarker(
        radius=1,
        weight=2.5,
        popup=cPopup,
        location=[cLong, cLati],
        color=cColor,
        opacity=1,
        fill_color=cColor,
        fill_opacity=0.1,        
        fill=True).add_to(mGroup)

# Inclui o controle de layers no mapa
folium.LayerControl(
        position="topright", 
        collapsed=False, 
        autoZIndex=True).add_to(fmap)

# Salva o mapa com os terremotos atualizados
fmap.save("earthquake.html")
# Abre o mapa com os terremotos atualizados no browser
webbrowser.open("earthquake.html")

#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#