import folium
def CadenaNueva(cadena):
    nuevaCadena=[]
    for i in cadena:
        i=i.split()
        i=[float(x) for x in i]
        i.reverse()
        nuevaCadena.append(tuple(i))
    return nuevaCadena
def coordenadas(path,G):
    contador1=0
    contador2=0
    Coordenadas=[]
    for i in range(len(path)):
        if i==len(path)-1:
            break
        elif path[i]!=path[i+1]:
            contador1+=G[path[i]][path[i+1]]['dist']
            contador2 += G[path[i]][path[i + 1]]['acoso']
            Coordenadas.extend(CadenaNueva(G[path[i]][path[i+1]]['Linestring']))
    print('Distancia: ',round(contador1/1000,1),' Km')
    print('Riesgo de Acoso: ',round(contador2/len(path),2))
    return Coordenadas
def crearMapa(camino,G,my_map,colour):
    Coordenadas1 = coordenadas(camino,G)
    folium.PolyLine(locations = [Coordenadas1],color=colour,
                    line_opacity = 0.5).add_to(my_map)
    return my_map
"""Linestring=['(-75.5524634, 6.2939397)', '(-75.5524634, 6.2939397)', '(-75.5519109, 6.2937299)']
print('Hasta aquí todo iba bien')
Coordenadas2=coordenadas(Linestring,G)
print(Coordenadas2)"""