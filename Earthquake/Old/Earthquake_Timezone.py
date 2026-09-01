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
import csv

# Arquivos de terremotos da internet
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.csv

# Obtem o diretório de trabalho para geracao do html 
cur_file = hos.path.abspath(__file__)
cur_dir = str.replace(hos.path.dirname(cur_file),"\\Earthquake","\\Earthquake\\Temp")
print(cur_dir)

# Monta o arquivo de dados em uma lista
def newList(nlist,nfile):
    for line in nfile:
        sline = str(line).replace("\n","")
        sline = sline.replace("'","")
        nline = sline.split(",")
        if nline[0] != "time":
            nlist.append(nline)

# Monta a lista de terremotos da semana com base no arquivo csv da internet 
# wfile = urllib.request.urlopen(".\2.5_week.csv")
wfile = csv.reader(open(".\week.csv", "r",encoding="UTF-8"))
wlist = []
newList(wlist,wfile)

# Monta a lista de terremotos do mes com base no arquivo csv da internet 
#mfile = urllib.request.urlopen(".\2.5_month.csv")
mfile = csv.reader(open(".\month.csv", "r",encoding="UTF-8"))
mlist = []
newList(mlist,mfile)

# Inverte a ordem dos terremotos os mais antigos primeiro 
wlist.reverse()
mlist.reverse()

# Cria o mapa base para os dados
fmap = folium.Map(location=[0, 0], 
                  zoom_start=2.5,
                  tiles="OpenStreetMap")

# Monta/Formata o estilo das bordas tectonicas no mapa
def tract_styles(feature):
    return {"fillColor": "green",
            "color": "brown",
            "weight": 1,
            "dashArray": "5, 5",
            "fillOpacity": 1,
            "opacity": 0.5}

# Inclui as bordas tectonicas no mapa
folium.GeoJson(".\Boundaries.json",
               name="Tectonics",
               style_function=tract_styles).add_to(fmap)

# Inclui o Equador, Tropicos and circulos Polares;
myLines = {"type": "FeatureCollection",
           "features": [
           {"type": "LineString","coordinates": [[360, 0], [-360, 0]], "popup": "Equator"},
           {"type": "LineString","coordinates": [[360, 23.43], [-360, 23,43]]},
           {"type": "LineString","coordinates": [[360, -23.43], [-360, -23.43]]},
           {"type": "LineString","coordinates": [[360, 66.56], [-360, 66.56]]},
           {"type": "LineString","coordinates": [[360, -66.56], [-360, -66.56]]}
         ]}

def tropics_styles(feature):
    return {"fillColor": "green",
            "color": "red",
            "weight": 1,
            "dashArray": "1, 1",
            "fillOpacity": 1,
            "opacity": 0.3}

folium.GeoJson(myLines, 
               name="Tropics",
               style_function=tropics_styles).add_to(fmap)

# Inclui os Fusos Horarios;
myLines = {"type": "FeatureCollection",
           "features": [
           {"type": "LineString","coordinates": [[0, 360], [0, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[15, 360], [15, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[30, 360], [30, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[45, 360], [45, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[60, 360], [60, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[75, 360], [75, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[90, 360], [90, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[105, 360], [105, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[120, 360], [120, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[135, 360], [135, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[150, 360], [150, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[165, 360], [165, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[180, 360], [180, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[195, 360], [195, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[210, 360], [210, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[225, 360], [225, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[240, 360], [240, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[255, 360], [255, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[270, 360], [270, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[285, 360], [285, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[300, 360], [300, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[315, 360], [315, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[330, 360], [330, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[345, 360], [345, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[360, 360], [360, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-15, 360], [-15, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-30, 360], [-30, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-45, 360], [-45, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-60, 360], [-60, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-75, 360], [-75, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-90, 360], [-90, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-105, 360], [-105, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-120, 360], [-120, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-135, 360], [-135, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-150, 360], [-150, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-165, 360], [-165, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-180, 360], [-180, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-195, 360], [-195, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-210, 360], [-210, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-225, 360], [-225, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-240, 360], [-240, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-255, 360], [-255, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-270, 360], [-270, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-285, 360], [-285, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-300, 360], [-300, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-315, 360], [-315, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-330, 360], [-330, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-345, 360], [-345, -360]], "popup": "UTC"},
           {"type": "LineString","coordinates": [[-360, 360], [-360, -360]], "popup": "UTC"}
         ]}

def timezone_styles(feature):
    return {"fillColor": "green",
            "color": "blue",
            "weight": 1,
            "dashArray": "1, 1",
            "fillOpacity": 1,
            "opacity": 0.2}

folium.GeoJson(myLines, 
               name="Time Zones",
               style_function=timezone_styles).add_to(fmap)

def circlemark(data,group,type):
    # Monta/Formata os dados/estilo dos terremotos no mapa
    cDate = data[0][1:11]
    cTime = data[0][11:22]
    cLong = float(data[1].strip())
    cLati = float(data[2].strip())
    cDeep = data[3].strip()
    cMag = float(data[4].strip())
    cRadius = pow(float(cMag),2) # * 10000
    cPlace = data[13].strip()
    cPopup = "Date:" + cDate + "\nTime:" + cTime + "\nMag:" + str(cMag) + "\nDeep:" + cDeep + "Km\nPlace:" + cPlace
    
    # Seleciona a cor (Today=red, Yesterday=orange, before=yellow)
    print(cDate)
    print(int(cDate[0:4]), int(cDate[5:7]), int(cDate[8:10]))
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
for row in wlist:
    print(row[0])
    if(row[0] != "[time"):
        circlemark(row,wgroup,"W")

# Cria um ponto no local do terremoto  
mgroup = folium.FeatureGroup(name='Earthquakes').add_to(fmap)
for row in mlist:
    if(row[0] != "[time"):
        circlemark(row,mgroup,"M")

# Cria um ponto no local do terremoto 
todaydt = "[" + str(datetime.datetime.today().date()) + " " + str(datetime.datetime.today().time()) 
cgroup = folium.FeatureGroup(name='Comments').add_to(fmap)
row = [todaydt,"90","0","0","0","0","0","0","0","0","0","0","0","Earth\nRead:Today\nOrange:Yesterday\nYellow:This_Week\nMagenta:This_Month"]
circlemark(row,cgroup,"C")
row = [todaydt,"-90","0","0","0","0","0","0","0","0","0","0","0","Earth\nFrom:Ekobots_Innovation_Ltda\nBy:Juan_Sirgado_y_Antico"]
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