import random

import plotly.express as px
import plotly.offline as pyo

import pandas as pd
import numpy as np

def interactive_graph(df: pd.DataFrame, clusters: str, elements: str):

    df_new = df.copy(deep = True)
    df_new = update_df(df_new, clusters)

    fig = px.scatter(df_new, 
                     x = 'X', 
                     y = 'Y', 
                     color = clusters,
                     labels = {'X': '', 'Y': ''},
                     hover_data = {'X': False, 'Y': False, clusters: True, elements: True},
                     )

    
    pyo.plot(fig, filename = 'clusters.html', auto_open = True)

def update_df(df_data: pd.DataFrame, clusters: str):
 
    # Добавляем новые пустые столбцы 'X' и 'Y'
    df_data['X'] = [None] * len(df_data)
    df_data['Y'] = [None] * len(df_data)
    a_list = list(range(-len(df_data[clusters].unique()),len(df_data[clusters].unique()),2))
    b_list = np.random.normal(1, 0.5, size=20)
    unique_values_dict = {value: None for value in df_data[clusters].unique()}
    for key, value in unique_values_dict.items():
        a = random.choice(a_list)
        a_list.remove(a)
        unique_values_dict[key] = a
    x_lst = []
    
    for x in range(-25,25,2):
        x_lst.append(x)
    y_lst = x_lst

        
    for key,value in unique_values_dict.items():
        ys = random.choice(x_lst)
        xs = random.choice(y_lst)
        if ys in y_lst:
            y_lst.remove(ys)
        if xs in y_lst:
            x_lst.remove(xs)

        for i in range(len(df_data[clusters])):
            if key == df_data[clusters][i]:

                df_data['X'][i] = xs + random.choice(b_list) + 1 
                df_data['Y'][i] = ys + random.choice(b_list) - 1
                
    return df_data


