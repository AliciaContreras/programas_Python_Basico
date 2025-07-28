print("--- Calculadora de Factorial (n!) ---")
print("El factorial de un número 'n' es el producto de todos los")
print("enteros positivos desde 1 hasta 'n'. Ejemplo: 5! = 1*2*3*4*5 = 120.")
print("Por definición, el factorial de 0 (0!) es 1.")
print("-" * 60)

try:
    numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
    if numero < 0:
        print("Error: El factorial solo se puede calcular para números no negativos.")
    else:
        print("\n--- 1. Cálculo con bucle 'for' ---")           
        resultado_for = 1
        if numero > 0: 
            for i in range(1, numero + 1):
                resultado_for *= i        
        print(f"El factorial de {numero}! (usando 'for') es: {resultado_for}")

        print("\n--- 2. Cálculo con bucle 'while' ---")        
        resultado_while = 1
        contador = 1
        
        while contador <= numero:
            resultado_while *= contador
            contador += 1    
        print(f"El factorial de {numero}! (usando 'while') es: {resultado_while}")

except ValueError:
    print("\nError: Entrada no válida. Por favor, ingrese un número entero.")

print("-" * 60)