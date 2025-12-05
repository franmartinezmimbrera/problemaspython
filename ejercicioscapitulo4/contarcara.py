# contarcara.py
def analizar_fichero():
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read() # Lee todo el contenido en una sola variable string
            
            total_caracteres = len(contenido)
            total_espacios = contenido.count(' ')
            
            print(f"Total de caracteres: {total_caracteres}")
            print(f"Total de espacios en blanco: {total_espacios}")
            
    except FileNotFoundError:
        print("El archivo no existe.")

if __name__ == "__main__":
    analizar_fichero()