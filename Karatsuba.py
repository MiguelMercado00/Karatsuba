# Multiplicación de números grandes con el algoritmo de Karatsuba
# Por Miguel Ángel Mercado Mercado
# Fecha: 31 de enero de 2024

def karatsuba(x, y) :
    # Si x o y son menores a 10, se realiza la multiplicación normal
    if x < 10 or y < 10 :
        return x * y
    else :
        # Se obtiene la longitud de los números
        n = max(len(str(x)), len(str(y)))
        # Se obtiene la mitad de la longitud
        m = n // 2
        # Se obtienen los números a, b, c y d
        a = x // 10**m
        b = x % 10**m
        c = y // 10**m
        d = y % 10**m
        # Se realiza la multiplicación de Karatsuba
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        adbc = karatsuba(a+b, c+d) - ac - bd
        return ac * 10**(2*m) + adbc * 10**m + bd

def main() :
    x = int(input("Ingrese un número: "))
    y = int(input("Ingrese otro número: "))
    print("El producto de", x, "y", y, "es", karatsuba(x, y))

main()