import pandas as pd
from matplotlib import pyplot as plt

cluster_final_completo = pd.read_csv("./clustersParaEstadisticoTodo.csv")

area_info = {}


cluster_0 = []
cluster_1 = []
cluster_2 = []

i_0U = 0
i_1U = 0
i_2U = 0
i_0R = 0
i_1R = 0
i_2R = 0

total_U = 0
total_R = 0

for i in range(len(cluster_final_completo['zona'])):
    # if(cluster_final_completo['ciudad'][i] in ciudades):
    try:
        if(cluster_final_completo['area'][i] == 'urbana'):
            if(cluster_final_completo['final'][i] == 0):
                i_0U += 1
            elif(cluster_final_completo['final'][i] == 1):
                i_1U += 1
            elif(cluster_final_completo['final'][i] == 2):
                i_2U += 1
            total_U += 1
        elif(cluster_final_completo['area'][i] == 'rural'):
            if(cluster_final_completo['final'][i] == 0):
                i_0R += 1
            elif(cluster_final_completo['final'][i] == 1):
                i_1R += 1
            elif(cluster_final_completo['final'][i] == 2):
                i_2R += 1
            total_R += 1
    except:
        pass

i_0U /= total_U
i_1U /= total_U
i_2U /= total_U
i_0R /= total_R
i_1R /= total_R
i_2R /= total_R

df = pd.DataFrame({'area': ['urbana', 'rural'], 'cluster_0': [i_0U,i_0R], 'cluster_1': [i_1U, i_1R], 'cluster_2': [i_2U, i_2R]})
ax = df[['cluster_0', 'cluster_1', 'cluster_2']].plot.bar(stacked=True, color = ['#636EFA', '#EF553B', '#00CC96'])
ax.set_xticklabels(df['area'])
plt.show()
            
       