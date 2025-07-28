print("--- Calculadora de Molaridad (M) ---")
print("La molaridad es una medida de la concentración de una solución.")
print("Fórmula: Molaridad (M) = Moles de soluto / Litros de solución")
print("-" * 55)

nombre_soluto = input("Ingrese el nombre del soluto (ej. Cloruro de Sodio): ")
moles_soluto = float(input(f"Ingrese los moles de {nombre_soluto}: "))
volumen_solucion_litros = float(input("Ingrese el volumen de la solución en litros (L): "))
es_experimento_formal_str = input("¿El cálculo es para un reporte de laboratorio formal? (s/n): ")
es_experimento_formal = es_experimento_formal_str.lower() == 's'

molaridad = moles_soluto / volumen_solucion_litros

print("\n--- Resumen del Cálculo ---")
print(f"Soluto analizado: {nombre_soluto} (Tipo: {type(nombre_soluto)})")
print(f"Moles de soluto: {moles_soluto} mol (Tipo: {type(moles_soluto)})")
print(f"Volumen de solución: {volumen_solucion_litros} L (Tipo: {type(volumen_solucion_litros)})")
print(f"¿Es para reporte formal?: {es_experimento_formal} (Tipo: {type(es_experimento_formal)})")
print("-" * 27)

print(f"La molaridad de la solución es: {molaridad:.4f} M")
print("-" * 27)

if es_experimento_formal:
    print("Recordatorio: Asegúrese de registrar este valor en su informe de laboratorio.")
else:
    print("Cálculo realizado con éxito para fines prácticos.")