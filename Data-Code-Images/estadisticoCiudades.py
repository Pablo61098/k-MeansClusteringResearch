import pandas as pd
from matplotlib import pyplot as plt

cluster_todo_completo = pd.read_csv("./clustersParaEstadisticoTodo.csv")


zona_info = {}

ciudades = [90150,230150,70150,130850,90750,170150,10150,180150,50150,110150,210150,220150,160150,140150,190150,200150,200350]

costa=[90150,230150,70150,130850,90750]
sierra=[170150,10150,180150,50150,110150]
oriente=[210150,220150,160150,140150,190150]
insular=[200150,200350]

for i in range(len(cluster_todo_completo['zona'])):
    if(cluster_todo_completo['ciudad'][i] in ciudades):
    # if(i<1000):
        try:
            if(cluster_todo_completo['final'][i] == 0):
                # print('0')
                zona_info[cluster_todo_completo['ciudad'][i]]['0'] += 1
                zona_info[cluster_todo_completo['ciudad'][i]]['total'] += 1
            elif(cluster_todo_completo['final'][i] == 1):
                # print('1')
                zona_info[cluster_todo_completo['ciudad'][i]]['1'] += 1
                zona_info[cluster_todo_completo['ciudad'][i]]['total'] += 1
            elif(cluster_todo_completo['final'][i] == 2):
                # print('2')
                zona_info[cluster_todo_completo['ciudad'][i]]['2'] += 1
                zona_info[cluster_todo_completo['ciudad'][i]]['total'] += 1
            # print(cluster_todo_completo['final'][i])
            # print('hey')
        except:
            # print('hey 2')
            if(cluster_todo_completo['final'][i] == 0):
                zona_info[cluster_todo_completo['ciudad'][i]] = {'0': 1, '1': 0, '2': 0, 'total': 1, 'zona': cluster_todo_completo['zona'][i]}
            elif(cluster_todo_completo['final'][i] == 1):
                zona_info[cluster_todo_completo['ciudad'][i]] = {'0': 0, '1': 1, '2': 0, 'total': 1, 'zona': cluster_todo_completo['zona'][i]}
            elif(cluster_todo_completo['final'][i] == 2):
                zona_info[cluster_todo_completo['ciudad'][i]] = {'0': 0, '1': 0, '2': 1, 'total': 1, 'zona': cluster_todo_completo['zona'][i]}
        
dataframe = {}
ciudades = []
cluster_0 = []
cluster_1 = []
cluster_2 = []
zonas = []
totales = []

todas_columnas_normalizar = [cluster_0, cluster_1, cluster_2, totales]

for key in zona_info:
    ciudades.append(key)
    cluster_0.append(zona_info[key]['0'])
    cluster_1.append(zona_info[key]['1'])
    cluster_2.append(zona_info[key]['2'])
    totales.append(zona_info[key]['total'])
    zonas.append(zona_info[key]['zona'])

for i in range(len(todas_columnas_normalizar)):
    if i != len(todas_columnas_normalizar) - 1:
        for j in range(len(todas_columnas_normalizar[i])):
            todas_columnas_normalizar[i][j] /=  todas_columnas_normalizar[-1][j]

dataframe['ciudad'] = ciudades
dataframe['cluster_0'] = cluster_0
dataframe['cluster_1'] = cluster_1
dataframe['cluster_2'] = cluster_2
dataframe['zona'] = zonas
dataframe['total'] = totales

dataframe = pd.DataFrame(dataframe)
# dataframe = dataframe.sort_values(by='total', ascending=False)
print(dataframe)
dataframe.to_csv('ciudadesPorCluster.csv', header=True, index=True)


ax = dataframe[['cluster_0', 'cluster_1', 'cluster_2']].plot.bar(stacked=True, color = ['#636EFA', '#EF553B', '#00CC96'] )
ax.set_xticklabels(['CUENCA', 'LATACUNGA', 'MACHALA', 'GUAYAQUIL', 'DURAN', 'LOJA', 'MANTA', 'MACAS', 'PUYO', 'QUITO', 'AMBATO', 'ZAMORA', 'P.B.MORENO', 'P.AYORA', 'NUEVA LOJA', 'EL COCA', 'S.DOMINGO'])
plt.show()

