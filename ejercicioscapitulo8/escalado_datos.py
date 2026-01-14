from sklearn.preprocessing import StandardScaler
import numpy as np
# Simulamos datos con escalas muy diferentes
# Ejemplo: [Edad (0-100), Salario (1000-50000)]
datos = np.array([
    [25, 30000],
    [50, 45000],
    [20, 15000],
    [35, 32000]
])
print("Datos originales:\n", datos)
# Inicializar el escalador
scaler = StandardScaler()
# Ajustar (calcular media y desviación) y transformar
datos_escalados = scaler.fit_transform(datos)
print("\nDatos estandarizados (Media~0, Var~1):\n", datos_escalados)
