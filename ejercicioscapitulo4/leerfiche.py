# leerfiche.py
def leer_fichero():
    try:
        # 'r' significa read (lectura)
        with open("datos.txt", "r", encoding="utf-8") as fichero:
            # Podemos iterar directamente sobre el objeto fichero
            for linea in fichero:
                print(linea.strip()) # strip() elimina el salto de línea doble
                
    except FileNotFoundError:
        print("El fichero 'datos.txt' no existe. Ejecuta el ejercicio anterior primero.")

if __name__ == "__main__":
    leer_fichero()