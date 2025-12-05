# fichero mayor.py
# Este programa calcula cuál es el número mayor de 10 introducidos por teclado 

def encontrar_mayor(lista_numeros):
    if not lista_numeros:
        return None
        
    mayor = lista_numeros[0]
    for num in lista_numeros:
        if num > mayor:
            mayor = num
    return mayor

if __name__ == "__main__":
    numeros = []
    print("Por favor, introduce 10 números enteros:")
    
    for i in range(10):
        val = int(input(f"Número {i+1}: "))
        numeros.append(val)
        
    el_mayor = encontrar_mayor(numeros)
    print(f"El número mayor introducido es: {el_mayor}")