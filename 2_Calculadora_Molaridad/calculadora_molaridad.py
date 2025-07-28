print("--- Calculadora de Concentración de Soluciones ---")
print("Este programa calcula Molaridad (M) y Normalidad (N).")
print("Fórmulas:")
print("  Moles = Gramos de soluto / Masa molar (g/mol)")
print("  Molaridad (M) = Moles / Litros de solución")
print("  Normalidad (N) = Molaridad * Número de equivalentes")
print("-" * 55)

nombre_soluto = input("Ingrese el nombre o fórmula del soluto (ej. NaOH): ").strip()

gramos_soluto = float(input(f"Ingrese los gramos de {nombre_soluto} pesados: "))

masa_molar = float(input(f"Ingrese la masa molar de {nombre_soluto} (g/mol): "))

volumen_solucion_litros = float(input("Ingrese el volumen final de la solución en litros (L): "))

moles_soluto = gramos_soluto / masa_molar

molaridad = moles_soluto / volumen_solucion_litros

print("\n--- Resultados del Cálculo de Molaridad ---")
print(f"Soluto analizado: {nombre_soluto} (Tipo: {type(nombre_soluto)})")
print(f"Gramos de soluto: {gramos_soluto} g (Tipo: {type(gramos_soluto)})")
print(f"Masa Molar: {masa_molar} g/mol (Tipo: {type(masa_molar)})")
print(f"Moles calculados: {moles_soluto:.4f} mol")
print("-" * 40)
print(f"La Molaridad (M) de la solución es: {molaridad:.4f} M")
print("-" * 40)

quiere_calcular_normalidad_str = input("\n¿Desea calcular también la Normalidad (N)? (s/n): ").lower()
quiere_calcular_normalidad = quiere_calcular_normalidad_str == 's'

if quiere_calcular_normalidad:
    print(f"\n Para calcular la Normalidad, se necesita el número de equivalentes (eq/mol).")
    print("Ejemplos: H₂SO₄ (ácido) tiene 2 eq/mol. NaOH (base) tiene 1 eq/mol.")

    equivalentes_por_mol = int(input(f"Ingrese el número de equivalentes para {nombre_soluto}: "))
    
    normalidad = molaridad * equivalentes_por_mol
    
    print("\n--- Resultado del Cálculo de Normalidad ---")
    print(f"Molaridad calculada: {molaridad:.4f} M")
    print(f"Número de equivalentes: {equivalentes_por_mol} eq/mol (Tipo: {type(equivalentes_por_mol)})")
    print(f"La Normalidad (N) de la solución es: {normalidad:.4f} N")
    print("-" * 40)
else:
    print("\nCálculo de Normalidad omitido.")

print("\nFin del programa.")