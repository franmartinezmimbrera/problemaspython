#fichero bisiesto.py
def es_bisiesto():
    try:
        anio = int(input("Introduce un año: "))
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"El año {anio} ES bisiesto.")
        else:
            print(f"El año {anio} NO es bisiesto.")
            
    except ValueError:
        print("Entrada no válida.")

if __name__ == "__main__":
    es_bisiesto()