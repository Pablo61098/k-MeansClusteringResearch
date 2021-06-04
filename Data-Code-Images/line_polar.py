import sklearn.cluster as cluster
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

flag_0 = True
if flag_0:

    for flag in range(6):
        data = pd.read_csv("./data_media_normal.csv")
        numero_clusters = 3
        namefile = ''
        if flag == 0:
            data = data.iloc[:, 3:]
            namefile = 'clustersTodo2.csv'
            # numero_clusters = 3
        elif flag == 1:
            data = data.iloc[:, 3:15]
            namefile = 'clustersResiduos2.csv'
            # numero_clusters = 3
        elif flag == 2:
            data = data.iloc[:, 15:26]
            namefile = 'clustersResiduosEspeciales2.csv'
            # numero_clusters = 5
        elif flag == 3:
            data = data.iloc[:, 26:34]
            namefile = 'clustersAgua2.csv'
            # numero_clusters = 5
        elif flag == 4:
            data = data.iloc[:, 34:41]
            namefile = 'clustersEnergia2.csv'
            # numero_clusters = 3
        elif flag == 5:
            data = data.iloc[:, 41:]
            namefile = 'clustersConciencia2.csv'
            # numero_clusters = 3



        kmeans = cluster.KMeans(n_clusters=numero_clusters, init="k-means++")
        kmeans.fit(data)
        clusters=pd.DataFrame(data,columns=data.columns)

        print(kmeans.cluster_centers_)
        # print(kmeans.labels_)
        # print(kmeans.inertia_)
        # print(kmeans.n_iter_)

        clusters['label']=kmeans.labels_
        # print('polar')
        # print(clusters)
        clusters.to_csv('./presentacion/'+namefile, header=True, index=False)
        polar=clusters.groupby("label").mean().reset_index()

        polar=pd.melt(polar,id_vars=["label"])

        fig = px.line_polar(polar, r="value", theta="variable", color="label", line_close=True,height=800,width=1400)
        
        fig.show()


        pie=clusters.groupby('label').size().reset_index()
        pie.columns=['label','value']
        fig2 = px.pie(pie,values='value',names='label',color='label')
        
        fig2.show()
else:
    namefile = 'clusterFinal2.csv'
    data = pd.read_csv('data_media_normal.csv')
    numero_clusters = 3
    data = data.iloc[:, 3:]


    kmeans = cluster.KMeans(n_clusters=numero_clusters, init="k-means++")
    kmeans.fit(data)
    clusters=pd.DataFrame(data,columns=data.columns)

    # print(kmeans.cluster_centers_)
    # print(kmeans.labels_)
    # print(kmeans.inertia_)
    # print(kmeans.n_iter_)

    clusters['label']=kmeans.labels_
    print('polar')
    print(clusters)
    clusters.to_csv(namefile, header=True, index=True)
    polar=clusters.groupby("label").mean().reset_index()

    polar=pd.melt(polar,id_vars=["label"])

    fig = px.line_polar(polar, r="value", theta="variable", color="label", line_close=True,height=800,width=1400)
    
    fig.show()


    pie=clusters.groupby('label').size().reset_index()
    pie.columns=['label','value']
    fig2 = px.pie(pie,values='value',names='label',color='label')
    
    fig2.show()

