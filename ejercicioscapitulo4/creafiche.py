# creafiche.py
def crear_fichero():
    try:
        # 'w' significa write (escritura). Si no existe, lo crea.
        with open("datos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Hola mundo.\n")
            archivo.write("Esto es una prueba de escritura en Python.\n")
            archivo.write("Python hace que el manejo de ficheros sea muy simple.\n")
        
        print("Archivo 'datos.txt' creado y escrito con éxito.")
        
    except IOError as e:
        print(f"Ocurrió un error al crear el archivo: {e}")

if __name__ == "__main__":
    crear_fichero()