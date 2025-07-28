def calcular_distancia(velocidad, tiempo):
    if velocidad >= 0 and tiempo >= 0:
        return velocidad * tiempo
    else:
        return None

def calcular_velocidad(distancia, tiempo):
    if tiempo > 0:
        return distancia / tiempo
    else:
        return None

def calcular_tiempo(distancia, velocidad):
    if velocidad > 0:
        return distancia / velocidad
    else:
        return None
def iniciar_calculadora():
    print("--- Calculadora de Cinemática (MRU) ---")

    while True:
        print("\n¿Qué variable deseas calcular?")
        print("1. Distancia (d = v * t)")
        print("2. Velocidad (v = d / t)")
        print("3. Tiempo (t = d / v)")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()

        try:
            if opcion == '1':
                v = float(input("Ingrese la velocidad (m/s): "))
                t = float(input("Ingrese el tiempo (s): "))
                distancia = calcular_distancia(v, t)
                if distancia is not None:
                    print(f"Resultado: La distancia es {distancia:.2f} metros.")
                else:
                    print("Error: La velocidad y el tiempo deben ser no negativos.")

            elif opcion == '2':
                d = float(input("Ingrese la distancia (metros): "))
                t = float(input("Ingrese el tiempo (s): "))
                velocidad = calcular_velocidad(d, t)
                if velocidad is not None:
                    print(f"Resultado: La velocidad es {velocidad:.2f} m/s.")
                else:
                    print("Error: El tiempo debe ser mayor que cero para calcular la velocidad.")

            elif opcion == '3':
                d = float(input("Ingrese la distancia (metros): "))
                v = float(input("Ingrese la velocidad (m/s): "))
                tiempo = calcular_tiempo(d, v)
                if tiempo is not None:
                    print(f"Resultado: El tiempo es {tiempo:.2f} segundos.")
                else:
                    print("Error: La velocidad debe ser mayor que cero para calcular el tiempo.")
            
            elif opcion == '4':
                print("¡Hasta luego!")
                break
            
            else:
                print("Error: Opción no válida. Por favor, elige un número del 1 al 4.")

        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese solo valores numéricos.")
        
        print("-" * 40)

if __name__ == "__main__":
    iniciar_calculadora()