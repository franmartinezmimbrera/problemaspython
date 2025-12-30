# escribefinal.py
def anadir_al_final():
    try:
        # 'a' significa append (añadir al final)
        with open("datos.txt", "a", encoding="utf-8") as fichero:
            fichero.write("\nEsta es una nueva línea insertada al final con Python.")
            print("Línea añadida correctamente.")
            
    except IOError:
        print("Error al abrir el archivo.")

if __name__ == "__main__":
    anadir_al_final()