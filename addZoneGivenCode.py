import pandas as pd


cluster_final = pd.read_csv("./clustersTodo.csv")
areas_ciudad = pd.read_csv("./data_adicional_normalizada.csv")
codigos = pd.read_csv("./codigosCantonParroquia.csv")

areas = areas_ciudad['area']
codigos_ciudades = areas_ciudad['ciudad']



cluster_final.insert(loc=0, column='area', value=areas)
cluster_final.insert(loc=1, column='ciudad', value=codigos_ciudades)


zonas = []

print(codigos['valor'])
codigos_zonas = list(codigos['valor'])

# j = 0
for i in range(len(cluster_final['ciudad'])):
    codigo = cluster_final['ciudad'][i]
    # print(codigo)
    if(codigo in codigos_zonas):
        fila_codigo = codigos_zonas.index(codigo)
        zona = codigos['categoria'][fila_codigo]
        zonas.append(zona)
        # j += 1
    else:
        zonas.append('N/A')
        
# print(j)

print(set(cluster_final['ciudad']))
print(len(set(cluster_final['ciudad'])))

cluster_final.insert(loc=, column='zona', value=zonas)
cluster_final.to_csv('clustersParaEstadisticoTodo.csv', header=True, index=False)
# cluster_final.to_csv('clustersFinalCompleto.csv', header=True, index=False)