from django.shortcuts import render
import folium
from pumaguaAPP.models import bebederos
from django.db.models import Q
from folium.plugins import LocateControl
import json
from folium.plugins import MarkerCluster
 
# Create your views here.
def index(request):
    datosBebederos = bebederos.objects.all()
    m = folium.Map(location=[19.320916010251914, -99.18395683244859], zoom_start=13,height="100%",width="90%",left="5%")
    LocateControl().add_to(m)
    
    html = ''' <h5> Nombre </h5> '''
    html1 = ''' <h5> Ubicacion </h5> '''
    
    
    marker_cluser = MarkerCluster().add_to(m)
    
    
    
    with open('pumaAgua/pumagua/rutasPumaBus.json') as jsonfile:
        paseoRutas = json.load(jsonfile)
    
    fg1 = folium.FeatureGroup(name="Ruta 1",show=False).add_to(m)
    folium.PolyLine(paseoRutas[0]['coordenadas'], tooltip="Ruta 1",color='#2CFF2C',stroke=True).add_to(fg1)
    
    fg2 = folium.FeatureGroup(name="Ruta 2",show=False).add_to(m)
    folium.PolyLine(paseoRutas[1]['coordenadas'], tooltip="Ruta 2",color='#fbbd3c',stroke=True).add_to(fg2)
       
    fg3 = folium.FeatureGroup(name="Ruta 3",show=False).add_to(m)
    folium.PolyLine(paseoRutas[2]['coordenadas'], tooltip="Ruta 3",color='#005E00',stroke=True).add_to(fg3)
    
    fg4 = folium.FeatureGroup(name="Ruta 4",show=False).add_to(m)
    folium.PolyLine(paseoRutas[3]['coordenadas'], tooltip="Ruta 4",color='#696969',stroke=True).add_to(fg4)
    
    fg5 = folium.FeatureGroup(name="Ruta 5",show=False).add_to(m)
    folium.PolyLine(paseoRutas[4]['coordenadas'], tooltip="Ruta 5",color='#1a76a9',stroke=True).add_to(fg5)
    
    fg6 = folium.FeatureGroup(name="Ruta 6",show=False).add_to(m)
    folium.PolyLine(paseoRutas[5]['coordenadas'], tooltip="Ruta 6",color='#bc131f',stroke=True).add_to(fg6)
    
    fg7 = folium.FeatureGroup(name="Ruta 7",show=False).add_to(m)
    folium.PolyLine(paseoRutas[6]['coordenadas'], tooltip="Ruta 7",color='#DC6C14',stroke=True).add_to(fg7)
    
    fg8 = folium.FeatureGroup(name="Ruta 8",show=False).add_to(m)
    folium.PolyLine(paseoRutas[7]['coordenadas'], tooltip="Ruta 8",color='#0a4ed2',stroke=True).add_to(fg8)
    
    fg9 = folium.FeatureGroup(name="Ruta 9",show=False).add_to(m)
    folium.PolyLine(paseoRutas[8]['coordenadas'], tooltip="Ruta 9",color='#FFA6D0',stroke=True).add_to(fg9)
    
    fg10 = folium.FeatureGroup(name="Ruta 10",show=False).add_to(m)
    folium.PolyLine(paseoRutas[9]['coordenadas'], tooltip="Ruta 10",color='#06414b',stroke=True).add_to(fg10)
    
    fg11 = folium.FeatureGroup(name="Ruta 11",show=False).add_to(m)
    folium.PolyLine(paseoRutas[10]['coordenadas'], tooltip="Ruta 11",color='#610B4B',stroke=True).add_to(fg11)
    
    fg12 = folium.FeatureGroup(name="Ruta 12",show=False).add_to(m)
    folium.PolyLine(paseoRutas[11]['coordenadas'], tooltip="Ruta 12",color='#e4c8d4',stroke=True).add_to(fg12)
    
    fg13 = folium.FeatureGroup(name="Ruta 13",show=False).add_to(m)
    folium.PolyLine(paseoRutas[12]['coordenadas'], tooltip="Ruta 13",color='#7dd83b',stroke=True).add_to(fg13)
    
    fg14 = folium.FeatureGroup(name="Bicipuma",show=False).add_to(m)
    folium.PolyLine(paseoRutas[13]['coordenadas'], tooltip="Ruta Bicipuma",color='#24c59b',stroke=True).add_to(fg14)
       
       
       
    folium.LayerControl().add_to(m)    
        
    
    
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(nombre__icontains=q)| Q(ubicacion__icontains=q)| Q(institucion__icontains=q)| Q(palabras_clave__icontains=q))
        data = bebederos.objects.filter(multiple_q)
        
        for coordenada in data:
            datos = (coordenada.latitud, coordenada.longitud)
            folium.Marker(datos, tooltip= 'Info', popup=html + coordenada.nombre + "\n" + html1 + coordenada.ubicacion + "\n",icon=folium.Icon(icon="glyphicon glyphicon-tint")).add_to(m)
    else:    
        for coordenada in datosBebederos:
            datos = (coordenada.latitud, coordenada.longitud)
            folium.Marker(datos, tooltip= 'Info', popup=html + coordenada.nombre + "\n" +  html1 + coordenada.ubicacion + "\n", icon=folium.Icon(icon="glyphicon glyphicon-tint"),name="Bebederos").add_to(marker_cluser)
    contexto = {'map': m._repr_html_()}
    
    return render(request, "index.html", contexto)
