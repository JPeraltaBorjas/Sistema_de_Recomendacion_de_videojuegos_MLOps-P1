import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI


# Indicamos título y descripción de la API
app = FastAPI(title='Proyecto Machine Learning Operations (MLOps) by Jay Peralta Borjas',
            description='API de datos y recomendaciones de juegos por usuario',)



# Cargamos los dataset
df_developer= pd.read_parquet('Dataset/df1_developer.parquet')


# Iniciamos la API
@app.get('/')
async def index():
    return 'Hola! Bienvenido a la API de recomedación. Por favor dirigite a /docs'



# Función informe historico por desarrollador
@app.get('/Desarrollador/')
def developer(desarrollador:str):

    """Se ingresa el nombre del desarrollador
    Devuelve como resultado un resumen de la cantidad de lanzamientos 
    y contenido Free to play por año"""

    # obtenemos el dataframe segun el desarrollador
    df_developer_filtrado= df_developer[df_developer['developer'] == desarrollador]

    # La cantidad de entregas que hay por año
    games_anio_ordenado= df_developer_filtrado.groupby('year')['id'].count().sort_index(ascending=False)
    games_anio_ordenado= games_anio_ordenado.reset_index()  # se convierte los indices en columnas 
    games_anio_ordenado.columns= ['Año','Cantidad de Items']  # cambiamos el nombre de las columnas

    # realizamos la agrupacion y contamos los elemnentos por año y por ser 'Free to Play' 
    contenido_free= df_developer_filtrado.groupby('year')['free'].value_counts(normalize=True).sort_index(ascending=False)*100
    contenido_free= contenido_free.reset_index()  # Se colocan los indices como columnas
    contenido_free= contenido_free[contenido_free['free'] == 'yes']  # Se realiza el filtro con solo los 'yes'
    contenido_free.columns= ['Año','yes_no','Contenido Free']  # Se cambia el nombre de las columnas
    
    # realizamos el juntar la tabla de las cantidad de items y porcentaje de contenido Free
    # tambien se realizan otras modificaciones al llenar con ceros los 'NaN', eliminacion de la columna 'yes_no'
    resultado= pd.merge(games_anio_ordenado, contenido_free, on='Año', how='left')
    resultado['Contenido Free']= resultado['Contenido Free'].fillna(0)
    resultado['Contenido Free']= resultado['Contenido Free'].apply(lambda x: str(round(x,2)) + '%')
    resultado['Año']= resultado['Año'].apply(lambda x: int(x))
    resultado.drop(columns= ['yes_no'], inplace= True)

    res={
        'Desarrollador': desarrollador,
        "Info": resultado.to_dict(orient='records')
    }
    
    return res