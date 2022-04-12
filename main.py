import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

"%matplotlib inline"

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#cargamos los datos de entrada
data = pd.read_csv('dataset.csv', low_memory=False)
#dimension y registros que contiene
print("shape")
print(data.shape)

#Veamos las primeras filas
print("head")
print(data.head())

#estadisticas de nuestros datos
print("describe")
print(data.describe())

print("show")
print(plt.show())

#filtrar datos
filtered_data = data[(data['Fecha de inicio de síntomas'] != '')& (data['Edad'] < 30)]
colores = ['orange', 'blue']
tamanios = [30, 60]

f1 = filtered_data['Fecha de inicio de síntomas'].values
f2 = filtered_data['Edad'].values
asignar = []

for i, row in filtered_data.iterrows():
    asignar.append(colores[0])
    
plt.scatter(f1, f2, c=asignar, s=tamanios[0])
print(plt.show())