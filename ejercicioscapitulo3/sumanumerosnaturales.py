# fichero sumanumerosnaturales.py
def suma_n_naturales():
    n = int(input("Introduce N (cantidad de números a sumar): "))
    suma = 0    
    for i in range(1, n + 1): #Suma n primeros números N con for
        suma += i        
    print(f"La suma de los primeros {n} números es: {suma}")
if __name__ == "__main__":
    suma_n_naturales()