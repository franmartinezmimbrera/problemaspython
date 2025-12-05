# fichero conteo.py
# Este ejercicio nos presenta la conversión de cadenas a letras mayúsculas y contar sus vocales

def procesar_cadenas():
    # Usamos una lista como si fuera un vector de strings
    frases = []
    
    print("Introduce 3 frases:")
    for i in range(3):
        frases.append(input(f"Frase {i+1}: "))
        
    vocales = "AEIOU"
    
    print("\n--- Resultados ---")
    for frase in frases:
        # Convertir a mayúsculas
        frase_upper = frase.upper()
        
        # Contar vocales
        num_vocales = 0
        for letra in frase_upper:
            if letra in vocales:
                num_vocales += 1
                
        print(f"Original: {frase}")
        print(f"Mayúsculas: {frase_upper}")
        print(f"Número de vocales: {num_vocales}")
        print("-" * 20)

if __name__ == "__main__":
    procesar_cadenas()