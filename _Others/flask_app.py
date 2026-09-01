#----------------------------------------------------------#
#             Program: Eartquake 2021/07/30                #
#               All rights reserved 2021                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             #
# Global map with recent earthquakes Week/Month            #
#----------------------------------------------------------#
# Site:                                                    #
# http://jsirgado.pythonanywhere.com/                      #
#----------------------------------------------------------#
from flask import Flask
app = Flask(__name__)
@app.route('/')
#----------------------------------------------------------#
# def hello_world():
#    return 'Hello from Flask!'
#----------------------------------------------------------#
def earthquake():

    import folium
    import urllib
    import datetime

    # Arquivos de terremotos da internet
    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv
    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv
    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv
    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.csv

    # Monta o arquivo de dados em uma lista
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
                "fillOpacity": 1}

    # Inclui as bordas tectonicas no mapa
    folium.GeoJson("https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json",
                name="Tectonics",
                style_function=tract_styles).add_to(fmap)

    def circlemark(data,group,type):
        # Monta/Formata os dados/estilo dos terremotos no mapa
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
        if difDays == 0:
            cColor = "red"
        elif difDays == 1:
            cColor = "orange"
        else:
            cColor = "yellow"
        if type == "M":
            cColor = "magenta"

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
        circlemark(row,wgroup,"W")

    # Cria um ponto no local do terremoto
    mgroup = folium.FeatureGroup(name='Earthquakes').add_to(fmap)
    for row in mlist:
        circlemark(row,mgroup,"M")

    # Inclui o controle de layers no mapa
    folium.LayerControl(
            position="topright",
            collapsed=False,
            autoZIndex=True).add_to(fmap)

    # Monta HTML do Mapa para apresentacao
    content = fmap.get_root().render()
    return content
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#