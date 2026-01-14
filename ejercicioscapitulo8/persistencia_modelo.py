import joblib
from sklearn.linear_model import LinearRegression

# Entrenar un modelo simple (ej. Doblar el número)
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

modelo = LinearRegression()
modelo.fit(X, y)

print("Predicción antes de guardar (input 5):", modelo.predict([[5]]))

# Guardar el modelo en un archivo (Persistencia)
nombre_fichero = 'modelo_regresion.pkl'
joblib.dump(modelo, nombre_fichero)
print(f"Modelo guardado en {nombre_fichero}")

#  Simular que estamos en otro script o programa...
# Borramos el modelo de la memoria para probar
del modelo

print("\nCargando modelo desde el disco...")
modelo_cargado = joblib.load(nombre_fichero)

#  Usar el modelo cargado
prediccion = modelo_cargado.predict([[5]])
print("Predicción con el modelo cargado (input 5):", prediccion)
