# creabinario.py
import pickle

def manejo_binario():
    # Definimos la estructura de datos (un diccionario en este caso)
    persona = {
        "id": 1,
        "nombre": "Juan Perez",
        "altura": 1.75
    }
    
    nombre_fichero = "registro.dat"

    # 1. Guardar en binario ('wb' = write binary)
    with open(nombre_fichero, "wb") as f_salida:
        pickle.dump(persona, f_salida)
        print("Datos guardados en binario.")

    # 2. Cargar del binario ('rb' = read binary)
    with open(nombre_fichero, "rb") as f_entrada:
        datos_recuperados = pickle.load(f_entrada)
        
        print("\n Datos recuperados del binario - Ahora en Memoria")
        print(f"ID: {datos_recuperados['id']}")
        print(f"Nombre: {datos_recuperados['nombre']}")
        print(f"Altura: {datos_recuperados['altura']}")

if __name__ == "__main__":
    manejo_binario()