# MLOps-P1: Proyecto Machine Learning Operations

El proyecto se centra en el desarrollo de una plataforma integral de análisis de datos y recomendaciones para una plataforma de entretenimiento. Se ha llevado a cabo un análisis detallado de los datos mediante el proceso ETL para garantizar la calidad y la integridad de los datos, seguido de un análisis exploratorio (EDA) para comprender mejor las tendencias y patrones. Este análisis ha proporcionado información crucial sobre el contenido de la plataforma y el comportamiento de los usuarios, fundamentando el desarrollo de las funciones de machine learning y el sistema de recomendaciones.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contacto](#contacto)

## Introducción

En la era digital actual, el análisis de datos y el aprendizaje automático (machine learning) han emergido como pilares fundamentales para la toma de decisiones informadas y el desarrollo de sistemas inteligentes. Desde la detección de patrones hasta la predicción de resultados, las aplicaciones del machine learning abarcan una amplia gama de campos, desde la medicina hasta la industria del entretenimiento.

Este proyecto fusiona la capacidad de realizar operaciones de machine learning con la funcionalidad de un sistema de recomendaciones, ofreciendo una solución versátil para diversas aplicaciones en la industria de los videojuegos.

## Instalación

Para el proyecto se ha valido de herramientas como python, librerias como pandas y numpy y archivos de comprensión de datos como los de formato '.parquet'. Todo esto para realizar de la mejor manera y de forma eficiente la importación de los datos y su manejo para obtener los resultados

### **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

También se han realizado y sustraido archivos pequeños esto con el motivo para realizar el trabajo más específico y con mucha mayor eficiencia, estos se encuentran en la carpeta Dataset.

---

### Análisis Realizado por ETL y EDA:

#### 1. **Análisis ETL (Extract, Transform, Load):**
   - Se realizó un proceso exhaustivo de ETL para extraer datos de múltiples fuentes, transformarlos en un formato adecuado y cargarlos en una base de datos centralizada.
   - Las etapas de extracción, transformación y carga se llevaron a cabo con el objetivo de garantizar la integridad, consistencia y calidad de los datos.
   - Se implementaron técnicas de limpieza y preprocesamiento de datos para abordar problemas como valores faltantes, duplicados y formatos inconsistentes.

#### 2. **Análisis EDA (Exploratory Data Analysis):**
   - Se realizó un análisis exploratorio de los datos para comprender mejor su estructura, distribución y características.
   - Se utilizaron visualizaciones y estadísticas descriptivas para identificar patrones, tendencias y relaciones en los datos.
   - Se llevaron a cabo análisis específicos para explorar la distribución de contenido por año, el comportamiento de compra de los usuarios y las preferencias de juego por género.

#### 3. **Conclusiones y Hallazgos:**
   - El análisis ETL y EDA proporcionó información valiosa sobre la calidad de los datos, así como insights significativos sobre el contenido disponible en la plataforma y el comportamiento de los usuarios.
   - Se identificaron áreas de mejora y oportunidades para optimizar las estrategias de negocio, mejorar la experiencia del usuario y aumentar la participación.
   - Los hallazgos obtenidos a partir del análisis ETL y EDA sirvieron como base para el desarrollo de las funciones de machine learning y el sistema de recomendaciones, asegurando que estén respaldadas por datos sólidos y análisis fundamentales.


## Uso
Se muestra en síntesis las funciones que se desarrollaron, junto con una descripción más detallada de cada una:

### Funciones del Proyecto:

#### 1. **developer(desarrollador: str)**
   Esta función devuelve la cantidad de ítems y el porcentaje de contenido gratuito por año, según la empresa desarrolladora.

   **Ejemplo de retorno:**
   ```
   | Año  | Cantidad de Items | Contenido Free  |
   |------|-------------------|------------------|
   | 2023 | 50                | 27%              |
   | 2022 | 45                | 25%              |
   | xxxx | xx                | xx%              |
   ```

#### 2. **userdata(User_id: str)**
   Esta función devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación basado en reviews.recommend y la cantidad de ítems.

   **Ejemplo de retorno:**
   ```
   {
       "Usuario X": "us213ndjss09sdf",
       "Dinero gastado": "200 USD",
       "% de recomendación": "20%",
       "cantidad de items": 5
   }
   ```

#### 3. **UserForGenre(genero: str)**
   Esta función devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

   **Ejemplo de retorno:**
   ```
   {
       "Usuario con más horas jugadas para Género X": "us213ndjss09sdf",
       "Horas jugadas": [
           {"Año": 2013, "Horas": 203},
           {"Año": 2012, "Horas": 100},
           {"Año": 2011, "Horas": 23}
       ]
   }
   ```

---

Estas funciones proporcionan funcionalidades clave para el proyecto, desde analizar el contenido según la empresa desarrolladora hasta proporcionar información detallada sobre el comportamiento del usuario y sus preferencias en el sistema de recomendaciones. 

## Características

1. **Análisis de Contenido por Desarrollador:**
   - Proporciona información detallada sobre la producción de contenido por año para una empresa desarrolladora específica.
   - Permite comprender la evolución del contenido a lo largo del tiempo y la proporción de contenido gratuito en relación con el total.
   - Útil para evaluar la estrategia de lanzamiento de la empresa y su enfoque en el contenido gratuito.

2. **Análisis de Comportamiento del Usuario:**
   - Ofrece una visión completa del comportamiento del usuario individual, incluyendo el gasto en la plataforma, el porcentaje de recomendación basado en reviews y la cantidad de ítems adquiridos.
   - Permite personalizar la experiencia del usuario y comprender mejor sus preferencias y patrones de consumo.
   - Fundamental para mejorar la retención de usuarios y optimizar las estrategias de recomendación.

3. **Análisis de Preferencias de Juego por Género:**
   - Identifica al usuario que ha acumulado más horas jugadas para un género de juego específico.
   - Proporciona información detallada sobre la distribución de horas jugadas por año para ese género en particular.
   - Ayuda a comprender las preferencias de juego de los usuarios y a adaptar las recomendaciones y ofertas en función de los géneros preferidos.

Estas características brindan una comprensión profunda tanto del contenido ofrecido en la plataforma como del comportamiento y las preferencias de los usuarios. Esto es esencial para mejorar la experiencia del usuario, optimizar las estrategias de negocio y maximizar la retención y la participación de los usuarios.


## Contacto

Jay Peralta Borjas - [jmw.peralta@gmail.com](mailto:jmw.peralta@gmail.com)

Link al proyecto en GitHub: https://github.com/JPeraltaBorjas/MLOps-P1.git