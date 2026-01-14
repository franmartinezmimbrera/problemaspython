import numpy as np
from sklearn.linear_model import LinearRegression
# Datos de ejemplo simple: y = 2x + 1
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)
# Realizar una predicción para un valor nuevo (x = 10)
nuevo_x = np.array([[10]])
prediccion = modelo.predict(nuevo_x)
print(f"Coeficiente (pendiente): {modelo.coef_[0]}")
print(f"Intercepto (ordenada): {modelo.intercept_}")
print(f"Predicción para x=10: {prediccion[0]}")
