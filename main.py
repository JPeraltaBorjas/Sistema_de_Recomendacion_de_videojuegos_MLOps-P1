import pandas as pd
import numpy as np
from fastapi import FastAPI


# Indicamos título y descripción de la API
app = FastAPI(title='Proyecto Machine Learning Operations (MLOps) by Jay Peralta Borjas',
            description='API de datos y recomendaciones de juegos por usuario',)



# Cargamos los dataset
df_developer= pd.read_parquet('Dataset/df1_developer.parquet')
df_userdata=pd.read_parquet('Dataset/df2_userdata.parquet')
df_UserForGenre_1=pd.read_parquet('Dataset/df3_UserForGenre_1.parquet')
df_UserForGenre_2=pd.read_parquet('Dataset/df3_UserForGenre_2.parquet')


# Iniciamos la API
@app.get('/')
async def index():
    return 'Hola! Bienvenido a la API de recomedación. Por favor dirigite a /docs'



# Función 1
@app.get('/desarrollador/')
def developer(desarrollador:str):

    """
    Se ingresa el nombre del desarrollador
    Devuelve como resultado un resumen de la cantidad de lanzamientos 
    y contenido Free to play por año
    """

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




# Función 2
@app.get('/userdata/')
def userdata(User_id:str):

    """
    Recibe como parametro el id del usuario
    Debe devolver `cantidad` de dinero gastado por el usuario, 
    el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.
    """

    condicion=(df_userdata['user_id'] == User_id)
    usuario=df_userdata[condicion]

    num_usuario='Usuario '+str(usuario.index[0] + 1)

    dinero_gastado=int(usuario.price.iloc[0])
    dinero_gastado=str(dinero_gastado) + ' USD'

    recomendacion=str(int(usuario.proportion.iloc[0])) + '%'

    cant_items=usuario.item_id.iloc[0]

    res={
        'Usuario '+str(usuario.index[0] + 1): User_id,
        "Dinero gastado": dinero_gastado,
        "porcentaje de recomendación": recomendacion,
        "cantidad de items": cant_items
    }
    return res



# Función 3
@app.get('/UserForGenre/')
def UserForGenre(genero:str):

    """ 
    Recibe como parametro de entrada el genero del juego
    devuelve el usuario que acumula más horas jugadas para el género dado 
    y una lista de la acumulación de horas jugadas por año de lanzamiento.
    """

    condicion_1= (df_UserForGenre_1['genres'] == genero)
    seleccion=df_UserForGenre_1[condicion_1]
    usuario=seleccion.iloc[0,1]
    tiempo_total=seleccion.iloc[0,2]

    condicion_2=(df_UserForGenre_2['genres'] == genero)&(df_UserForGenre_2['user_id'] == usuario)
    tiempo_anio=df_UserForGenre_2[condicion_2]
    tiempo_anio=tiempo_anio.loc[:,['year','playtime_forever']].sort_values('year',ascending=False)
    tiempo_anio.columns=['Año','Horas']

    anios_dict = tiempo_anio.to_dict(orient='records')

    res={
        'Usuario con más horas jugadas para el Género ' + genero: usuario,
        'Hojas jugadas': anios_dict
    }

    return res
