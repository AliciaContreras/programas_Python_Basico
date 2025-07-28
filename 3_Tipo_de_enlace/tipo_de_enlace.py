print("--- Clasificador de Tipo de Enlace Químico ---")
print("El tipo de enlace (iónico, covalente polar, covalente no polar)")
print("se puede predecir con la diferencia de electronegatividad (ΔEN).")
print("\nValores de referencia comunes:")
print(" - Iónico:         ΔEN ≥ 1.7")
print(" - Covalente Polar:  0.4 < ΔEN < 1.7")
print(" - Covalente No Polar: ΔEN ≤ 0.4")
print("-" * 50)

try:
    nombre_atomo1 = input("Ingrese el símbolo del primer átomo (ej. H, O, Na): ").strip()
    electro_atomo1 = float(input(f"Ingrese la electronegatividad de {nombre_atomo1}: "))

    nombre_atomo2 = input("Ingrese el símbolo del segundo átomo (ej. Cl, F, C): ").strip()
    electro_atomo2 = float(input(f"Ingrese la electronegatividad de {nombre_atomo2}: "))

    diferencia_electronegatividad = abs(electro_atomo1 - electro_atomo2)

    diferencia_electronegatividad = round(diferencia_electronegatividad, 2)

    print(f"\nLa diferencia de electronegatividad (ΔEN) entre {nombre_atomo1} y {nombre_atomo2} es: {diferencia_electronegatividad}")
    print("-" * 50)

    if diferencia_electronegatividad >= 1.7:
        tipo_enlace = "Iónico"
        explicacion = "En este tipo de enlace, hay una transferencia casi completa de electrones de un átomo a otro, formando iones."

    elif diferencia_electronegatividad > 0.4:
        tipo_enlace = "Covalente Polar"
        explicacion = "Los electrones se comparten de manera desigual, creando una carga parcial positiva en un átomo y una negativa en el otro."

    else:
        tipo_enlace = "Covalente No Polar"
        explicacion = "Los electrones se comparten de manera casi equitativa entre los dos átomos."
        
        if diferencia_electronegatividad == 0:
            explicacion += " Al ser la diferencia cero, es un enlace covalente 'puro'."

    print(f"Resultado Predicho: El enlace es predominantemente {tipo_enlace}.")
    print("\nExplicación:")
    print(explicacion)

except ValueError:
    print("\nError: La electronegatividad debe ser un valor numérico.")
except Exception as e:
    print(f"\nOcurrió un error inesperado: {e}")
print("-" * 50)