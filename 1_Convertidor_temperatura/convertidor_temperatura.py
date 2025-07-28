print("--- Conversor de Unidades de Temperatura ---")
print("Este programa convierte grados Celsius a Fahrenheit y Kelvin.")
print("-" * 45)

grados_celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit = (grados_celsius * 9/5) + 32
celsius_a_kelvin = grados_celsius + 273.15
print("\n--- Resultados de la Conversión ---")
print(f"{grados_celsius}°C equivalen a {celsius_a_fahrenheit:.2f}°F (Fahrenheit).")
print(f"{grados_celsius}°C equivalen a {celsius_a_kelvin:.2f}K (Kelvin).")
print("-" * 45)