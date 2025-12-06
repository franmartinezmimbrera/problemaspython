# leerfiche.py
def leer_fichero():
    try:
        # 'r' significa read (lectura)
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            print("--- Contenido del archivo ---")
            # Podemos iterar directamente sobre el objeto archivo
            for linea in archivo:
                print(linea.strip()) # strip() elimina el salto de línea doble
                
    except FileNotFoundError:
        print("El archivo 'datos.txt' no existe. Ejecuta el ejercicio anterior primero.")

if __name__ == "__main__":
    leer_fichero()