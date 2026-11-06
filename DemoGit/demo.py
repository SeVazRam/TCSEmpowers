def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def main():
    print("=== Calculadora sencilla funciones ===")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print(f"Suma: {sumar(a, b)}")
    print(f"Resta: {restar(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")

if __name__ == "__main__":
    main()
