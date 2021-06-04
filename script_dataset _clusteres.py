import pandas as pd

data1 = pd.read_csv("clustersResiduos.csv")
data2 = pd.read_csv("clustersResiduosEspeciales.csv")
data3 = pd.read_csv("clustersAgua.csv")
data4 = pd.read_csv("clustersEnergia.csv")
data5 = pd.read_csv("clustersConciencia.csv")

clusters1 = list(data1['label'])
clusters2 = list(data2['label'])
clusters3 = list(data3['label'])
clusters4 = list(data4['label'])
clusters5 = list(data5['label'])

tabla = [clusters1, clusters2, clusters3, clusters4, clusters5]

for i in range(len(tabla)):

    for j in range(len(clusters1)):

        dato = int(tabla[i][j])

        if (i == 0):
            if (dato == 0):
                tabla[i][j] = 2
            elif (dato  == 1):
                tabla[i][j] = 0
            else:
                tabla[i][j] = 1
        
        elif (i == 1):
            if (dato == 0):
                pass
            elif (dato  == 1):
                tabla[i][j] = 2
            else:
                tabla[i][j] = 1

        elif (i == 2):
            if (dato == 0):
                tabla[i][j] = 2
            elif (dato  == 1):
                pass
            else:
                tabla[i][j] = 0

        elif (i == 3):
            if (dato == 0):
                pass
            elif (dato  == 1):
                tabla[i][j] = 2
            else:
                tabla[i][j] = 1

        else:
            if (dato == 0):
                tabla[i][j] = 2
            elif (dato  == 1):
                tabla[i][j] = 0
            else:
                tabla[i][j] = 1

diccionario = {'residuos': clusters1, 'residuos_especiales': clusters2, 'agua': clusters3, 'energia': clusters4, 'conciencia': clusters5}

dataframe = pd.DataFrame(diccionario)
dataframe.to_csv('clustersFinal.csv', header=True, index=True)