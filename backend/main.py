import folium
import matplotlib.pyplot as plt
import pandas as pd
from branca.element import Figure
import geopandas
import networkx
import numpy as np
import osmnx as ox
import os
import sys
'''
fig3= Figure(width=550,height=350)
m3=folium.Map(location=[12.84243, 80.06048],tiles='cartodbpositron',zoom_start=11)
fig3.add_child(m3)

#Adding markers to the map
folium.Marker(location=[12.9632, 80.2459],popup='Apollo Speciality Hospital',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[13.0877, 80.1856],popup='<strong>Frontier Lifeline Hospital, ChennaiFrontier Lifeline Hospital</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[13.0861, 80.1874],popup='madras medical mission coordinates',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[13.0758, 80.2273],popup='<strong>billroth hospitals coordinates</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[13.05711, 80.19422],popup='JJ Hospital',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[13.05159, 80.21144],popup='SRM Hospital',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[13.06061, 80.24334],popup='<strong>MedIndia Hospitals</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[13.06318, 80.2516],popup='Apollo Hospital ',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[13.06099, 80.27481],popup='<strong>Triplicane Government Hospital</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[13.04327, 80.27241],popup='CSI Kalyani Hospital',tooltip='Click here to see Popup').add_to(m3)


m3.save('Final22.html')'''

#-----------------------------------------------------------------------------------------------------------------------------
#Funtion for addinf lat and long

import pandas as pd

# assign data of lists.
data = {'LAT': [12.9632, 13.0877, 13.0861, 13.0758, 13.05711, 13.05159, 13.06061, 13.06318, 13.06099],
        'LON': [80.2459, 80.1856, 80.1874, 80.2273, 80.19422, 80.21144, 80.24334, 80.2516, 80.27481],
        'NAME': ['Apollo Speciality Hospital', 'Frontier Lifeline Hospital', 'madras medical mission coordinates',
                 'billroth hospitals coordinates', 'JJ Hospital', 'SRM Hospital', 'Apollo Hospital', 'Triplicane Government Hospital', 'CSI Kalyani Hospital']}


df = pd.DataFrame(data)
#---------------------------------------------------------------------------------------------------------------------------------

def calci(x1, y1, x2, y2):
    dist = np.sqrt(np.power((x1 - x2), 2) + np.power((y1 - y2), 2))
    return dist


def shortest(LAT, LON, df):
    df['Rank'] = calci(LAT, LON, df['LAT'], df['LON'])
    df = df.sort_values('Rank')
    print(df)
    Best = df.iloc[0]
    return Best


def Runner(LAT, LON):
    Best = shortest(LAT, LON, df)
    INP = [LAT,LON]
    DEST = [Best.LAT,Best.LON]
    closest_nodes = ox.distance.nearest_nodes(graph, INP, DEST)

    closest_rows = nodes.loc[closest_nodes]
    od_nodes = geopandas.GeoDataFrame(closest_rows, geometry='geometry', crs=nodes.crs)

    shortest_route = networkx.shortest_path(G=graph, source=closest_nodes[0], target=closest_nodes[1], weight='length')

    # fig, ax = ox.plot_graph_route(graph, shortest_route, figsize=(15, 15))

    # Save the figure
    # fig.savefig("my_graph.png")
    X = []
    y = []
    for i in shortest_route:
        a, b = graph.nodes[i]['x'], graph.nodes[i]['y']
        X.append(a)
        y.append(b)
    mf = pd.DataFrame({'Lat': X , 'Long' : y})
    mf
    return mf,Best


def mapper(a,b,c,d,e):
    fig3 = Figure(width=550, height=350)
    m3 = folium.Map(location=[12.84243, 80.06048], tiles='cartodbpositron', zoom_start=11)
    fig3.add_child(m3)
    folium.Marker(location=[a,b],popup='initial_loc',tooltip='Initial').add_to(m3)
    folium.Marker(location=[c,d],popup=f'<strong>{e}</strong>',tooltip='<strong>Final</strong>').add_to(m3)
    
   
    
    
    m3.save('Final22.html')
    
    source_html = "Final22.html"
    destination_directory = "/ResQroute/frontend/public"
    filename = "final.html"
    destination_path = os.path.join(destination_directory, filename)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    try:
        with open(source_html, "r", encoding="utf-8") as source_file:
            html_content = source_file.read()
    except Exception as e:
        print(e)
    try:
        with open(destination_path, "w", encoding="utf-8") as destination_file:
            destination_file.write(html_content)
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------
#Oynx
graph = ox.graph_from_point((13.0877, 80.1856), dist=600, network_type='all')
nodes, edges = ox.graph_to_gdfs(graph)

#Folium
fig3= Figure(width=550,height=350)
m3=folium.Map(location=[12.84243, 80.06048],tiles='cartodbpositron',zoom_start=11)
fig3.add_child(m3)
#----------------------------------------------------------------------------------------------------------------------------------

LON, LAT=80.046855, 12.8249087
Alert , Locs = Runner(LON, LAT)
print(Alert)
print(Locs)
mapper(LAT, LON,Locs.LAT,Locs.LON,Locs.NAME)



