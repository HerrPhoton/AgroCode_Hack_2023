from itertools import combinations
import random

import numpy as np
import pandas as pd

import networkx as nx

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as pyo


def create_interactive_graph(clusters, elements):

    unique_clusters = np.unique(clusters)
    #cluster_centers = np.random.ran
 
    # Создаем граф
    graph = nx.Graph()

    # Добавляем узлы и рёбра
    for u,v in combinations(elements, 2):
        graph.add_edge(u, v)
   
    # Создание интерактивной визуализации
    positions = {element : [] for element in np.unique(elements)}

    for pos_element in positions:
        for element,x,y in zip(Element,X,Y):
            if element == pos_element:
                positions[pos_element].append((x, y))
    
    node_x = []
    node_y = []

    for names in Element:
        for node in graph.nodes():
            if names == node:
                x,y = positions[node][0]
                node_x.append(x)
                node_y.append(y)
                del positions[node][0]
            continue
      
    node_trace = go.Scatter(x = node_x, 
                            y = node_y,
                            mode = 'markers',
                            hoverinfo = 'text',
                            marker=dict(
                                showscale = True,
                                colorscale = 'Rainbow',
                                size = 10,
                                colorbar = dict(
                                    thickness = 15,
                                    title = 'Кластеры',
                                    xanchor = 'left',
                                    titleside = 'right'
            )
        )
    )
    
    cluster_mapping = {cluster: i for i, cluster in enumerate(set(Cluster))}
    Cluster_numeric = [cluster_mapping[cluster] for cluster in Cluster]

    node_adjacencies = []
    node_text = []

    for i in range(len(Element)):
        node_adjacencies.append(Cluster_numeric[i])
        node_text.append(f'Кластер: {Cluster[i]}, Элемент: {Element[i]}')

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = make_subplots(rows = 1, cols = 1)
    fig.add_trace(node_trace, row = 1, col = 1)
    fig.update_layout(showlegend = False)

    pyo.plot(fig, filename='clusters.html', auto_open = True)

def update_df(df_data):
 
    # Добавляем новые пустые столбцы 'X' и 'Y'
    df_data['X'] = [None] * len(df_data)
    df_data['Y'] = [None] * len(df_data)

    # print(df_data)
    iter = 0
    for cls in df_data['Cluster'].unique():
        for i in range(len(df_data['Cluster'])):
            if cls == df_data['Cluster'][i]:
                df_data['X'][i] = random.uniform(iter - 1,iter)
                df_data['Y'][i] = random.uniform(iter - 1,iter)
        iter+=1
    

    return df_data

def main_work(df):
    # Создаем списки для каждого столбца
    df_new = update_df(df)
    # print(df_new)
    Cluster = df_new['predict'].tolist()
    Element = df_new['title'].tolist()
    X = np.zeros_like(Cluster)
    Y = np.zeros_like(Cluster)

    create_interactive_graph(Cluster, Element, X, Y)


