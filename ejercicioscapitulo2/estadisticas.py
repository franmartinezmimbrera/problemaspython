# fichero estadisticas.py 
# Este programa calcula estadísticas sobre alumnos

try:
    print("Introduce el número de alumnos por categoría:")
    suspensos = int(input("Suspensos: "))
    aprobados = int(input("Aprobados (5-6): "))
    notables = int(input("Notables (7-8): "))
    sobresalientes = int(input("Sobresalientes (9-10): "))
    total_alumnos = suspensos + aprobados + notables + sobresalientes
    
    # Verificamos si hay alumnos para evitar dividir por cero
    if total_alumnos == 0:
        print("\nNo hay alumnos en la clase. No se pueden calcular estadísticas.")
    else:
        superan = aprobados + notables + sobresalientes
        porc_superan = (superan / total_alumnos) * 100
        porc_suspensos = (suspensos / total_alumnos) * 100
        porc_notables = (notables / total_alumnos) * 100
        porc_sobresalientes = (sobresalientes / total_alumnos) * 100
        porc_aprobados_strict = (aprobados / total_alumnos) * 100
        
        print(f"\nTotal alumnos: {total_alumnos}")
        print(f"% que superan la asignatura: {porc_superan:.2f}%")
        print(f"% de suspensos:              {porc_suspensos:.2f}%")
        print(f"% de notables:               {porc_notables:.2f}%")
        print(f"% de sobresalientes:         {porc_sobresalientes:.2f}%")
        print(f"% de aprobados (nota 5-6):   {porc_aprobados_strict:.2f}%")
        
except ValueError:
    print("Error: Debes introducir números enteros válidos.")