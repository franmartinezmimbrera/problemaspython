#fichero newton.py
#Calcula mediante el binomio de newton los datos datos

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def combinatorio(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def binomio_newton(a, b, n):
    print(f"Desarrollo de ({a} + {b})^{n} = ", end="")
    resultado_total = 0
    
    for k in range(n + 1):
        comb = combinatorio(n, k)
        termino = comb * (a**(n-k)) * (b**k)
        resultado_total += termino
        
        if k > 0:
            print(" + ", end="")
        print(f"{comb}*{a}^{n-k}*{b}^{k}", end="")
        
    print(f"\nResultado calculado suma total: {resultado_total}")
    print(f"Comprobación directa ((a+b)^n): {(a+b)**n}")

if __name__ == "__main__":
    binomio_newton(2, 3, 4)