import pandas as pd

# Carga de un archivo CSV
# Supongamos que tenemos un archivo llamado 'viviendas.csv' en la misma carpeta
# Si no tienes uno, puedes usar esta URL de un dataset real de viviendas:
url = "viviendas.csv"
#"https://raw.githubusercontent.com/ageron/
# handson-ml2/master/datasets/housing/housing.csv"

try:
    # Leemos el archivo CSV
    df = pd.DataFrame()
    df = pd.read_csv(url)  #Puede ser una ruta local o una url
    
    # Exploración inicial
    print(" Dimensiones del dataset (Filas, Columnas) ")
    print(df.shape)
    
    print("\n Listado de columnas")
    print(df.columns.tolist())
    #  Mostrar las primeras filas
    print("\nPrimeras filas del dataset de viviendas ")
    print(df.head())
    # Conteo de valores en una variable categórica
    # Esto es útil para saber cuántas casas hay cerca del mar, en el interior, etc.
    print("\n Distribución por cercanía al océano ")
    print(df['ocean_proximity'].value_counts())
    
    # Guardar una copia local si se desea
    df.to_csv("copia_viviendas.csv", index=False)
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
