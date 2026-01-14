from sklearn.metrics import accuracy_score, confusion_matrix
# (Asumimos que las variables y_test y predicciones vienen del ejercicio anterior)
# Para este ejemplo, creamos datos simulados:
y_real      = [0, 1, 1, 0, 2, 2, 1, 0]
y_predichos = [0, 1, 0, 0, 2, 1, 1, 0] # Algunos errores intencionados

# Calcular Accuracy (Exactitud)
acc = accuracy_score(y_real, y_predichos)
print(f"Exactitud del modelo: {acc:.2f} ({acc*100}%)")

# Matriz de confusión
# Muestra: filas (realidad) vs columnas (predicción)
matriz = confusion_matrix(y_real, y_predichos)
print("\nMatriz de Confusión:\n", matriz)
