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

import folium
import urllib
import webbrowser
import datetime 
import os as hos


txt_from = "\nFrom:Ekobots_Innovation_Ltda"
txt_by = "\nBy:Juan_Sirgado_y_Antico"

# Obtem o diretório de trabalho para geracao do html 
cur_file = hos.path.abspath(__file__)
cur_dir = str.replace(hos.path.dirname(cur_file),"\\Earthquake","\\Earthquake\\Temp")
# print(cur_dir)

# Monta o arquivo de dados em uma lista
#----------------------------------------------------------#
def newList(nlist,nfile):
    for line in nfile:
        sline = str(line.decode("utf-8")).replace("\n","")
        nline = sline.split(",")
        if nline[0] != "time":
            nlist.append(nline)

# Monta a lista de terremotos da semana com base no arquivo csv da internet 
wfile = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv")
wlist = []
newList(wlist,wfile)

# Monta a lista de terremotos do mes com base no arquivo csv da internet 
mfile = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv")
mlist = []
newList(mlist,mfile)

# Inverte a ordem dos terremotos os mais antigos primeiro 
wlist.reverse()
mlist.reverse()

# Define your configuration
gmap = ""
todaydt = str(datetime.datetime.today().date()) + " " + str(datetime.datetime.today().time())[0:8] 
API_KEY = "cb1_28yc_1_984182b7f210fa5ea4150122"
tile_url = f"https://a.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}.png?key={API_KEY}"
attr_url = "<p>Red:Today<br>Orange:Yesterday<br>Yellow:This_Week<br>Magenta:This_Month</p>"
attr_url += f"<p>earthquake.usgs.gov<br>OpenStreetMap.org<br>basemaps.cartocdn.com<br>{todaydt}</p>"
name_url = "LAYERS"

# 2. Initialize the map
fmap = folium.Map(tiles=None,
                  location=[0,0],
                  zoom_start=2.5)

folium.TileLayer(
    tiles=tile_url,
    attr=attr_url,
    name=name_url).add_to(fmap)

# Monta/Formata o estilo das bordas tectonicas no mapa
#----------------------------------------------------------#
def tract_styles(feature):
    return {"fillColor": "green",
            "fillOpacity": 1,
            "color": "brown",
            "opacity": 0.5,
            "weight": 1,
            "dashArray": "5, 5"}

# Inclui as bordas tectonicas no mapa
folium.GeoJson(".\\GeoJSON\\tectonicplates_boundaries.geojson",
               name="Tectonic",
               style_function=tract_styles).add_to(fmap)

# Monta/Formata o estilo das linhas geográficas no mapa
#----------------------------------------------------------#
def line_styles(feature):
    return {"fillColor": "green",
            "fillOpacity": 1,
            "color": "blue",
            "opacity": 0.2,
            "weight": 1}

# Inclui as linhas geograficas no mapa
folium.GeoJson(".\\GeoJSON\\geographic_lines.geojson",
               name="Geographic",
               style_function=line_styles).add_to(fmap)

# Monta/Formata os dados/estilo dos terremotos no mapa
#----------------------------------------------------------#
def circlemark(data,group,type):
    cDate = data[0][0:10]
    cTime = data[0][11:22]
    cLong = float(data[1].strip())
    cLati = float(data[2].strip())
    cDeep = data[3].strip()
    cMag = float(data[4].strip())
    cRadius = pow(float(cMag),2) # * 10000
    cPlace = data[13].strip()
    cPopup = "Date:" + cDate + "\nTime:" + cTime + "\nMag:" + str(cMag) + "\nDeep:" + cDeep + "Km\nPlace:" + cPlace
    
    # Seleciona a cor (Today=red, Yesterday=orange, before=yellow)
    dInput = datetime.date(int(cDate[0:4]), int(cDate[5:7]), int(cDate[8:10]))
    dToday = datetime.datetime.today().date()
    # dToday = datetime.datetime.utcnow().date()
    difDays = (dToday - dInput).days
    if type == "M":
        cColor = "magenta"
    elif type == "W":
        if difDays == 0: 
            cColor = "red"
        elif difDays == 1: 
            cColor = "orange"
        else: 
            cColor = "yellow"
    elif type == "C":
        cColor = "black"

    # Cria o circulo/ponto marcando o epicentro do terremoto  
    folium.CircleMarker(
        radius=1 if type == "M" else cRadius,
        weight=3 if type == "M" else 1,
        popup=cPopup,
        location=[cLong, cLati],
        color=cColor,
        opacity=1,
        fill_color=cColor,
        fill_opacity=0.1,        
        fill=True).add_to(group)
    return

# Cria o circulo baseado na magnetude do terremoto  
wgroup = folium.FeatureGroup(name='Magnitude').add_to(fmap)
#----------------------------------------------------------#
for row in wlist:
    circlemark(row,wgroup,"W")

# Cria um ponto no local do terremoto  
mgroup = folium.FeatureGroup(name='Earthquakes').add_to(fmap)
#----------------------------------------------------------#
for row in mlist:
    circlemark(row,mgroup,"M")

# Cria um ponto no local do terremoto 
#----------------------------------------------------------#
cgroup = folium.FeatureGroup(name='Comments').add_to(fmap)
row = [todaydt,"90","0","0","0","0","0","0","0","0","0","0","0","\nNorth_Pole"]
circlemark(row,cgroup,"C")
row = [todaydt,"-90","0","0","0","0","0","0","0","0","0","0","0","\nSouth_Pole" + txt_from + txt_by]
circlemark(row,cgroup,"C")

# Inclui o controle de layers no mapa
folium.LayerControl(
        position="topright", 
        collapsed=False, 
        autoZIndex=True).add_to(fmap)

# Salva o mapa com os terremotos atualizados
fmap.save(cur_dir + "\\earthquake.html")

# Abre o mapa com os terremotos atualizados no browser
webbrowser.open(cur_dir + "\\earthquake.html")

#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#