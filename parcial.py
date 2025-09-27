import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfcanciones=pd.read_csv("spotify-2023.csv",encoding="latin1")
dfcanciones.head(10)

#PUNTO A :Cargue los datos e identifique cuantas variables categóricas (tipo object) y cuantas
#variables numéricas tiene#
dfcanciones.info()
cantidad=("la cantidad de datos numericos es: 17 la cantidad de datos de texto es: 7")
print(cantidad)
dfcanciones[["track_name","released_year","released_month","mode",]].head(5)

#PUNTO B: Desarrolle un algoritmo que nos diga cuantas canciones de Coldplay hay en la base
#de datos.Filtra las canciones que hay de Coldplay en la nase de datos#

def filtroColdplay(dfcanciones):
    dfFiltroColdplay = dfcanciones[dfcanciones["artist(s)_name"] == 'Coldplay']
    return dfFiltroColdplay
dfColdplay = filtroColdplay(dfcanciones)
dfColdplay
contadorColdplay = dfColdplay['artist(s)_name'].count()
print("hay:",contadorColdplay)

#PUNTO C:Encuentre el máximo y el mínimo de cada columna numérica en la base de datos
a= dfcanciones.select_dtypes(include=np.number).max()
print("el maximo es:")
print(a)

b = dfcanciones.select_dtypes(include=np.number).min()
print("el minimo es:")
print(b)

#PUNTO D:Desarrolle una función que reciba como parámetro su base de datos y un artista y le
#devuelva todas las canciones de ese artista en base de datos.
artistas=str(input("ingrese el nombre del artista:"))
def canciones(df, artista):
    return df[df["artist(s)_name"] == artista]

print(canciones(dfcanciones, artistas))

#PUNTO E: Cree una tabla con una función de agregación, que muestre la sumatoria de cuantas
#canciones Taylor Swift y Coldplay aparecen en playlist


def filtrocoldplay(dfcanciones):
    dfFiltrocoldplay = dfcanciones[dfcanciones["artist(s)_name"] == 'Coldplay']
    return dfFiltrocoldplay
dfColdplay = filtrocoldplay(dfcanciones)
dfColdplay
contadorColdplay = dfColdplay['artist(s)_name'].count()
print("canciones de coldplay:",contadorColdplay)

def filtroTaylor(dfcanciones):
    dfFiltroTaylor = dfcanciones[dfcanciones["artist(s)_name"] == 'Taylor Swift']
    return dfFiltroTaylor
dfTaylor = filtroTaylor(dfcanciones)
dfTaylor
contadorTaylor = dfTaylor['artist(s)_name'].count()
print("canciones de taylor:",contadorTaylor)   

total= contadorColdplay + contadorTaylor

tabla = pd.DataFrame({
    'Artista': ['Coldplay', 'Taylor Swift', 'Total'],
    'Cantidad de Canciones': [contadorColdplay, contadorTaylor, total]
})

print(tabla)

#F. Desarrolle un subplot con dos gráficos, el primero es un boxplot relacione artist_count
#(eje x) con streams, y el segundo un histograma de los años de lanzamiento.



