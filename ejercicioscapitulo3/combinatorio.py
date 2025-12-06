# fichero combinatorio.py
# Calcula el número combinatorio C(n, r) o n sobre r, usando factoriales.
# Reutilizamos la lógica del factorial
def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

def combinatorio(n, m):
    if m > n:
        return 0
    # Formula: N! / (M! * (N-M)!)
    return factorial(n) // (factorial(m) * factorial(n - m))

if __name__ == "__main__":
    try:
        n = int(input("Introduce N: "))
        m = int(input("Introduce M: "))
        print(f"El combinatorio de {n} sobre {m} es: {combinatorio(n, m)}")
    except ValueError:
        print("Entrada inválida.")