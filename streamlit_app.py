import streamlit as st

# Configuración básica de la pestaña
st.set_page_config(page_title="Portafolio de Alicia", page_icon="💻")

# ==========================================
# DEFINICIONES GLOBALES (Tus funciones y listas)
# ==========================================

# --- DATOS PARA TABLA PERIÓDICA ---
ELEMENTOS_QUIMICOS = [
    {"numero_atomico": 1, "simbolo": "H", "nombre": "Hidrógeno", "masa_atomica": 1.008, "tipo": "No metal"},
    {"numero_atomico": 2, "simbolo": "He", "nombre": "Helio", "masa_atomica": 4.0026, "tipo": "Gas noble"},
    {"numero_atomico": 3, "simbolo": "Li", "nombre": "Litio", "masa_atomica": 6.94, "tipo": "Metal alcalino"},
    {"numero_atomico": 4, "simbolo": "Be", "nombre": "Berilio", "masa_atomica": 9.0122, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 5, "simbolo": "B", "nombre": "Boro", "masa_atomica": 10.81, "tipo": "Metaloide"},
    {"numero_atomico": 6, "simbolo": "C", "nombre": "Carbono", "masa_atomica": 12.011, "tipo": "No metal"},
    {"numero_atomico": 7, "simbolo": "N", "nombre": "Nitrógeno", "masa_atomica": 14.007, "tipo": "No metal"},
    {"numero_atomico": 8, "simbolo": "O", "nombre": "Oxígeno", "masa_atomica": 15.999, "tipo": "No metal"},
    {"numero_atomico": 9, "simbolo": "F", "nombre": "Flúor", "masa_atomica": 18.998, "tipo": "Halógeno"},
    {"numero_atomico": 10, "simbolo": "Ne", "nombre": "Neón", "masa_atomica": 20.180, "tipo": "Gas noble"},
    {"numero_atomico": 11, "simbolo": "Na", "nombre": "Sodio", "masa_atomica": 22.990, "tipo": "Metal alcalino"},
    {"numero_atomico": 12, "simbolo": "Mg", "nombre": "Magnesio", "masa_atomica": 24.305, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 13, "simbolo": "Al", "nombre": "Aluminio", "masa_atomica": 26.982, "tipo": "Otro metal"},
    {"numero_atomico": 14, "simbolo": "Si", "nombre": "Silicio", "masa_atomica": 28.085, "tipo": "Metaloide"},
    {"numero_atomico": 15, "simbolo": "P", "nombre": "Fósforo", "masa_atomica": 30.974, "tipo": "No metal"},
    {"numero_atomico": 16, "simbolo": "S", "nombre": "Azufre", "masa_atomica": 32.06, "tipo": "No metal"},
    {"numero_atomico": 17, "simbolo": "Cl", "nombre": "Cloro", "masa_atomica": 35.45, "tipo": "Halógeno"},
    {"numero_atomico": 18, "simbolo": "Ar", "nombre": "Argón", "masa_atomica": 39.948, "tipo": "Gas noble"},
    {"numero_atomico": 19, "simbolo": "K", "nombre": "Potasio", "masa_atomica": 39.098, "tipo": "Metal alcalino"},
    {"numero_atomico": 20, "simbolo": "Ca", "nombre": "Calcio", "masa_atomica": 40.078, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 21, "simbolo": "Sc", "nombre": "Escandio", "masa_atomica": 44.956, "tipo": "Metal de transición"},
    {"numero_atomico": 22, "simbolo": "Ti", "nombre": "Titanio", "masa_atomica": 47.867, "tipo": "Metal de transición"},
    {"numero_atomico": 23, "simbolo": "V", "nombre": "Vanadio", "masa_atomica": 50.942, "tipo": "Metal de transición"},
    {"numero_atomico": 24, "simbolo": "Cr", "nombre": "Cromo", "masa_atomica": 51.996, "tipo": "Metal de transición"},
    {"numero_atomico": 25, "simbolo": "Mn", "nombre": "Manganeso", "masa_atomica": 54.938, "tipo": "Metal de transición"},
    {"numero_atomico": 26, "simbolo": "Fe", "nombre": "Hierro", "masa_atomica": 55.845, "tipo": "Metal de transición"},
    {"numero_atomico": 27, "simbolo": "Co", "nombre": "Cobalto", "masa_atomica": 58.933, "tipo": "Metal de transición"},
    {"numero_atomico": 28, "simbolo": "Ni", "nombre": "Níquel", "masa_atomica": 58.693, "tipo": "Metal de transición"},
    {"numero_atomico": 29, "simbolo": "Cu", "nombre": "Cobre", "masa_atomica": 63.546, "tipo": "Metal de transición"},
    {"numero_atomico": 30, "simbolo": "Zn", "nombre": "Zinc", "masa_atomica": 65.38, "tipo": "Metal de transición"},
    {"numero_atomico": 31, "simbolo": "Ga", "nombre": "Galio", "masa_atomica": 69.723, "tipo": "Otro metal"},
    {"numero_atomico": 32, "simbolo": "Ge", "nombre": "Germanio", "masa_atomica": 72.630, "tipo": "Metaloide"},
    {"numero_atomico": 33, "simbolo": "As", "nombre": "Arsénico", "masa_atomica": 74.922, "tipo": "Metaloide"},
    {"numero_atomico": 34, "simbolo": "Se", "nombre": "Selenio", "masa_atomica": 78.971, "tipo": "No metal"},
    {"numero_atomico": 35, "simbolo": "Br", "nombre": "Bromo", "masa_atomica": 79.904, "tipo": "Halógeno"},
    {"numero_atomico": 36, "simbolo": "Kr", "nombre": "Kriptón", "masa_atomica": 83.798, "tipo": "Gas noble"},
    {"numero_atomico": 37, "simbolo": "Rb", "nombre": "Rubidio", "masa_atomica": 85.468, "tipo": "Metal alcalino"},
    {"numero_atomico": 38, "simbolo": "Sr", "nombre": "Estroncio", "masa_atomica": 87.62, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 39, "simbolo": "Y", "nombre": "Itrio", "masa_atomica": 88.906, "tipo": "Metal de transición"},
    {"numero_atomico": 40, "simbolo": "Zr", "nombre": "Zirconio", "masa_atomica": 91.224, "tipo": "Metal de transición"},
    {"numero_atomico": 41, "simbolo": "Nb", "nombre": "Niobio", "masa_atomica": 92.906, "tipo": "Metal de transición"},
    {"numero_atomico": 42, "simbolo": "Mo", "nombre": "Molibdeno", "masa_atomica": 95.96, "tipo": "Metal de transición"},
    {"numero_atomico": 43, "simbolo": "Tc", "nombre": "Tecnecio", "masa_atomica": 98.0, "tipo": "Metal de transición"},
    {"numero_atomico": 44, "simbolo": "Ru", "nombre": "Rutenio", "masa_atomica": 101.07, "tipo": "Metal de transición"},
    {"numero_atomico": 45, "simbolo": "Rh", "nombre": "Rodio", "masa_atomica": 102.91, "tipo": "Metal de transición"},
    {"numero_atomico": 46, "simbolo": "Pd", "nombre": "Paladio", "masa_atomica": 106.42, "tipo": "Metal de transición"},
    {"numero_atomico": 47, "simbolo": "Ag", "nombre": "Plata", "masa_atomica": 107.87, "tipo": "Metal de transición"},
    {"numero_atomico": 48, "simbolo": "Cd", "nombre": "Cadmio", "masa_atomica": 112.41, "tipo": "Metal de transición"},
    {"numero_atomico": 49, "simbolo": "In", "nombre": "Indio", "masa_atomica": 114.82, "tipo": "Otro metal"},
    {"numero_atomico": 50, "simbolo": "Sn", "nombre": "Estaño", "masa_atomica": 118.71, "tipo": "Otro metal"},
    {"numero_atomico": 51, "simbolo": "Sb", "nombre": "Antimonio", "masa_atomica": 121.76, "tipo": "Metaloide"},
    {"numero_atomico": 52, "simbolo": "Te", "nombre": "Telurio", "masa_atomica": 127.60, "tipo": "Metaloide"},
    {"numero_atomico": 53, "simbolo": "I", "nombre": "Yodo", "masa_atomica": 126.90, "tipo": "Halógeno"},
    {"numero_atomico": 54, "simbolo": "Xe", "nombre": "Xenón", "masa_atomica": 131.29, "tipo": "Gas noble"},
    {"numero_atomico": 55, "simbolo": "Cs", "nombre": "Cesio", "masa_atomica": 132.91, "tipo": "Metal alcalino"},
    {"numero_atomico": 56, "simbolo": "Ba", "nombre": "Bario", "masa_atomica": 137.33, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 57, "simbolo": "La", "nombre": "Lantano", "masa_atomica": 138.91, "tipo": "Lantánido"},
    {"numero_atomico": 58, "simbolo": "Ce", "nombre": "Cerio", "masa_atomica": 140.12, "tipo": "Lantánido"},
    {"numero_atomico": 59, "simbolo": "Pr", "nombre": "Praseodimio", "masa_atomica": 140.91, "tipo": "Lantánido"},
    {"numero_atomico": 60, "simbolo": "Nd", "nombre": "Neodimio", "masa_atomica": 144.24, "tipo": "Lantánido"},
    {"numero_atomico": 61, "simbolo": "Pm", "nombre": "Prometio", "masa_atomica": 145.0, "tipo": "Lantánido"},
    {"numero_atomico": 62, "simbolo": "Sm", "nombre": "Samario", "masa_atomica": 150.36, "tipo": "Lantánido"},
    {"numero_atomico": 63, "simbolo": "Eu", "nombre": "Europio", "masa_atomica": 151.96, "tipo": "Lantánido"},
    {"numero_atomico": 64, "simbolo": "Gd", "nombre": "Gadolinio", "masa_atomica": 157.25, "tipo": "Lantánido"},
    {"numero_atomico": 65, "simbolo": "Tb", "nombre": "Terbio", "masa_atomica": 158.93, "tipo": "Lantánido"},
    {"numero_atomico": 66, "simbolo": "Dy", "nombre": "Disprosio", "masa_atomica": 162.50, "tipo": "Lantánido"},
    {"numero_atomico": 67, "simbolo": "Ho", "nombre": "Holmio", "masa_atomica": 164.93, "tipo": "Lantánido"},
    {"numero_atomico": 68, "simbolo": "Er", "nombre": "Erbio", "masa_atomica": 167.26, "tipo": "Lantánido"},
    {"numero_atomico": 69, "simbolo": "Tm", "nombre": "Tulio", "masa_atomica": 168.93, "tipo": "Lantánido"},
    {"numero_atomico": 70, "simbolo": "Yb", "nombre": "Iterbio", "masa_atomica": 173.05, "tipo": "Lantánido"},
    {"numero_atomico": 71, "simbolo": "Lu", "nombre": "Lutecio", "masa_atomica": 174.97, "tipo": "Lantánido"},
    {"numero_atomico": 72, "simbolo": "Hf", "nombre": "Hafnio", "masa_atomica": 178.49, "tipo": "Metal de transición"},
    {"numero_atomico": 73, "simbolo": "Ta", "nombre": "Tántalo", "masa_atomica": 180.95, "tipo": "Metal de transición"},
    {"numero_atomico": 74, "simbolo": "W", "nombre": "Wolframio", "masa_atomica": 183.84, "tipo": "Metal de transición"},
    {"numero_atomico": 75, "simbolo": "Re", "nombre": "Renio", "masa_atomica": 186.21, "tipo": "Metal de transición"},
    {"numero_atomico": 76, "simbolo": "Os", "nombre": "Osmio", "masa_atomica": 190.23, "tipo": "Metal de transición"},
    {"numero_atomico": 77, "simbolo": "Ir", "nombre": "Iridio", "masa_atomica": 192.22, "tipo": "Metal de transición"},
    {"numero_atomico": 78, "simbolo": "Pt", "nombre": "Platino", "masa_atomica": 195.08, "tipo": "Metal de transición"},
    {"numero_atomico": 79, "simbolo": "Au", "nombre": "Oro", "masa_atomica": 196.97, "tipo": "Metal de transición"},
    {"numero_atomico": 80, "simbolo": "Hg", "nombre": "Mercurio", "masa_atomica": 200.59, "tipo": "Metal de transición"},
    {"numero_atomico": 81, "simbolo": "Tl", "nombre": "Talio", "masa_atomica": 204.38, "tipo": "Otro metal"},
    {"numero_atomico": 82, "simbolo": "Pb", "nombre": "Plomo", "masa_atomica": 207.2, "tipo": "Otro metal"},
    {"numero_atomico": 83, "simbolo": "Bi", "nombre": "Bismuto", "masa_atomica": 208.98, "tipo": "Otro metal"},
    {"numero_atomico": 84, "simbolo": "Po", "nombre": "Polonio", "masa_atomica": 209.0, "tipo": "Metaloide"},
    {"numero_atomico": 85, "simbolo": "At", "nombre": "Astato", "masa_atomica": 210.0, "tipo": "Metaloide"},
    {"numero_atomico": 86, "simbolo": "Rn", "nombre": "Radón", "masa_atomica": 222.0, "tipo": "Gas noble"},
    {"numero_atomico": 87, "simbolo": "Fr", "nombre": "Francio", "masa_atomica": 223.0, "tipo": "Metal alcalino"},
    {"numero_atomico": 88, "simbolo": "Ra", "nombre": "Radio", "masa_atomica": 226.0, "tipo": "Metal alcalinotérreo"},
    {"numero_atomico": 89, "simbolo": "Ac", "nombre": "Actinio", "masa_atomica": 227.0, "tipo": "Actínido"},
    {"numero_atomico": 90, "simbolo": "Th", "nombre": "Torio", "masa_atomica": 232.04, "tipo": "Actínido"},
    {"numero_atomico": 91, "simbolo": "Pa", "nombre": "Protactinio", "masa_atomica": 231.04, "tipo": "Actínido"},
    {"numero_atomico": 92, "simbolo": "U", "nombre": "Uranio", "masa_atomica": 238.03, "tipo": "Actínido"},
    {"numero_atomico": 93, "simbolo": "Np", "nombre": "Neptunio", "masa_atomica": 237.0, "tipo": "Actínido"},
    {"numero_atomico": 94, "simbolo": "Pu", "nombre": "Plutonio", "masa_atomica": 244.0, "tipo": "Actínido"},
    {"numero_atomico": 95, "simbolo": "Am", "nombre": "Americio", "masa_atomica": 243.0, "tipo": "Actínido"},
    {"numero_atomico": 96, "simbolo": "Cm", "nombre": "Curio", "masa_atomica": 247.0, "tipo": "Actínido"},
    {"numero_atomico": 97, "simbolo": "Bk", "nombre": "Berkelio", "masa_atomica": 247.0, "tipo": "Actínido"},
    {"numero_atomico": 98, "simbolo": "Cf", "nombre": "Californio", "masa_atomica": 251.0, "tipo": "Actínido"},
    {"numero_atomico": 99, "simbolo": "Es", "nombre": "Einstenio", "masa_atomica": 252.0, "tipo": "Actínido"},
    {"numero_atomico": 100, "simbolo": "Fm", "nombre": "Fermio", "masa_atomica": 257.0, "tipo": "Actínido"},
    {"numero_atomico": 101, "simbolo": "Md", "nombre": "Mendelevio", "masa_atomica": 258.0, "tipo": "Actínido"},
    {"numero_atomico": 102, "simbolo": "No", "nombre": "Nobelio", "masa_atomica": 259.0, "tipo": "Actínido"},
    {"numero_atomico": 103, "simbolo": "Lr", "nombre": "Lawrencio", "masa_atomica": 262.0, "tipo": "Actínido"},
    {"numero_atomico": 104, "simbolo": "Rf", "nombre": "Rutherfordio", "masa_atomica": 267.0, "tipo": "Metal de transición"},
    {"numero_atomico": 105, "simbolo": "Db", "nombre": "Dubnio", "masa_atomica": 268.0, "tipo": "Metal de transición"},
    {"numero_atomico": 106, "simbolo": "Sg", "nombre": "Seaborgio", "masa_atomica": 271.0, "tipo": "Metal de transición"},
    {"numero_atomico": 107, "simbolo": "Bh", "nombre": "Bohrio", "masa_atomica": 272.0, "tipo": "Metal de transición"},
    {"numero_atomico": 108, "simbolo": "Hs", "nombre": "Hasio", "masa_atomica": 277.0, "tipo": "Metal de transición"},
    {"numero_atomico": 109, "simbolo": "Mt", "nombre": "Meitnerio", "masa_atomica": 276.0, "tipo": "Metal de transición"},
    {"numero_atomico": 110, "simbolo": "Ds", "nombre": "Darmstatio", "masa_atomica": 281.0, "tipo": "Metal de transición"},
    {"numero_atomico": 111, "simbolo": "Rg", "nombre": "Roentgenio", "masa_atomica": 280.0, "tipo": "Metal de transición"},
    {"numero_atomico": 112, "simbolo": "Cn", "nombre": "Copernicio", "masa_atomica": 285.0, "tipo": "Metal de transición"},
    {"numero_atomico": 113, "simbolo": "Nh", "nombre": "Nihonio", "masa_atomica": 284.0, "tipo": "Otro metal"},
    {"numero_atomico": 114, "simbolo": "Fl", "nombre": "Flerovio", "masa_atomica": 289.0, "tipo": "Otro metal"},
    {"numero_atomico": 115, "simbolo": "Mc", "nombre": "Moscovio", "masa_atomica": 288.0, "tipo": "Otro metal"},
    {"numero_atomico": 116, "simbolo": "Lv", "nombre": "Livermorio", "masa_atomica": 293.0, "tipo": "Otro metal"},
    {"numero_atomico": 117, "simbolo": "Ts", "nombre": "Teneso", "masa_atomica": 294.0, "tipo": "Halógeno"},
    {"numero_atomico": 118, "simbolo": "Og", "nombre": "Oganesón", "masa_atomica": 294.0, "tipo": "Gas noble"}
]


# --- FUNCIONES PARA MRU (Tus funciones originales) ---
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

# ==========================================
# MENÚ DE NAVEGACIÓN
# ==========================================
st.sidebar.title("Mis Prácticas de Python")
opcion = st.sidebar.selectbox(
    "Selecciona un código para ejecutar:",
    ("1. Convertidor Temperatura", 
     "2. Calculadora Molaridad", 
     "3. Tipo de Enlace", 
     "4. Calculadora Factorial", 
     "5. Tabla Periódica", 
     "6. MRU")
)

# ==========================================
# CÓDIGO 1: CONVERTIDOR DE TEMPERATURA
# ==========================================
if opcion == "1. Convertidor Temperatura":
    st.header("1_Convertidor_temperatura")
    st.text("--- Conversor de Unidades de Temperatura ---")
    st.text("Este programa convierte grados Celsius a Fahrenheit y Kelvin.")
    st.text("-" * 45)

    # Input
    grados_celsius = st.number_input("Por favor, ingrese la temperatura en grados Celsius:", value=0.0)

    if st.button("Ejecutar Conversión"):
        # Tu lógica original
        celsius_a_fahrenheit = (grados_celsius * 9/5) + 32
        celsius_a_kelvin = grados_celsius + 273.15
        
        # Tus prints originales adaptados
        st.write("--- Resultados de la Conversión ---")
        st.write(f"{grados_celsius}°C equivalen a {celsius_a_fahrenheit:.2f}°F (Fahrenheit).")
        st.write(f"{grados_celsius}°C equivalen a {celsius_a_kelvin:.2f}K (Kelvin).")
        st.text("-" * 45)

# ==========================================
# CÓDIGO 2: CALCULADORA MOLARIDAD
# ==========================================
elif opcion == "2. Calculadora Molaridad":
    st.header("2_Calculadora_Molaridad")
    st.text("--- Calculadora de Concentración de Soluciones ---")
    st.text("Fórmulas: Moles = g/Mm | M = mol/L | N = M * eq")
    
    # Inputs (Adaptados de tus inputs originales)
    nombre_soluto = st.text_input("Ingrese el nombre o fórmula del soluto (ej. NaOH):", value="NaOH")
    gramos_soluto = st.number_input(f"Ingrese los gramos de {nombre_soluto} pesados:", min_value=0.0, format="%.4f")
    masa_molar = st.number_input(f"Ingrese la masa molar de {nombre_soluto} (g/mol):", min_value=0.0001, format="%.4f")
    volumen_solucion_litros = st.number_input("Ingrese el volumen final de la solución en litros (L):", min_value=0.0001, format="%.4f")

    # Checkbox para simular tu pregunta "s/n" de normalidad
    quiere_calcular_normalidad = st.checkbox("¿Desea calcular también la Normalidad (N)?")
    
    equivalentes_por_mol = 1
    if quiere_calcular_normalidad:
        st.text("Para calcular la Normalidad, se necesita el número de equivalentes.")
        equivalentes_por_mol = st.number_input(f"Ingrese el número de equivalentes para {nombre_soluto}:", min_value=1, step=1)

    if st.button("Calcular"):
        # Tu lógica original
        moles_soluto = gramos_soluto / masa_molar
        molaridad = moles_soluto / volumen_solucion_litros

        st.write("\n--- Resultados del Cálculo de Molaridad ---")
        st.write(f"Soluto analizado: {nombre_soluto}")
        st.write(f"Gramos de soluto: {gramos_soluto} g")
        st.write(f"Masa Molar: {masa_molar} g/mol")
        st.write(f"Moles calculados: {moles_soluto:.4f} mol")
        st.text("-" * 40)
        st.success(f"La Molaridad (M) de la solución es: {molaridad:.4f} M")
        st.text("-" * 40)

        if quiere_calcular_normalidad:
            normalidad = molaridad * equivalentes_por_mol
            st.write("\n--- Resultado del Cálculo de Normalidad ---")
            st.write(f"Molaridad calculada: {molaridad:.4f} M")
            st.write(f"Número de equivalentes: {equivalentes_por_mol} eq/mol")
            st.success(f"La Normalidad (N) de la solución es: {normalidad:.4f} N")
            st.text("-" * 40)
        else:
            st.write("\nCálculo de Normalidad omitido.")
            
        st.write("\nFin del programa.")

# ==========================================
# CÓDIGO 3: TIPO DE ENLACE
# ==========================================
elif opcion == "3. Tipo de Enlace":
    st.header("3_Tipo_de_enlace")
    st.text("--- Clasificador de Tipo de Enlace Químico ---")
    st.text("Valores: Iónico (>=1.7), Cov. Polar (>0.4), Cov. No Polar (<=0.4)")
    st.text("-" * 50)

    # He mantenido tu bloque try-except original dentro del botón
    nombre_atomo1 = st.text_input("Ingrese el símbolo del primer átomo:", "H")
    electro_atomo1 = st.number_input(f"Ingrese la electronegatividad de {nombre_atomo1}:", value=0.0)

    nombre_atomo2 = st.text_input("Ingrese el símbolo del segundo átomo:", "Cl")
    electro_atomo2 = st.number_input(f"Ingrese la electronegatividad de {nombre_atomo2}:", value=0.0)

    if st.button("Determinar Enlace"):
        try:
            # Tu lógica original exacta
            diferencia_electronegatividad = abs(electro_atomo1 - electro_atomo2)
            diferencia_electronegatividad = round(diferencia_electronegatividad, 2)

            st.write(f"\nLa diferencia de electronegatividad (ΔEN) entre {nombre_atomo1} y {nombre_atomo2} es: {diferencia_electronegatividad}")
            st.text("-" * 50)

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

            st.success(f"Resultado Predicho: El enlace es predominantemente {tipo_enlace}.")
            st.write("\nExplicación:")
            st.write(explicacion)

        except ValueError:
            st.error("\nError: La electronegatividad debe ser un valor numérico.")
        except Exception as e:
            st.error(f"\nOcurrió un error inesperado: {e}")
        
        st.text("-" * 50)

# ==========================================
# CÓDIGO 4: CALCULADORA FACTORIAL
# ==========================================
elif opcion == "4. Calculadora Factorial":
    st.header("4_Calculadora_factorial")
    st.text("--- Calculadora de Factorial (n!) ---")
    st.text("Ejemplo: 5! = 1*2*3*4*5 = 120.")
    st.text("-" * 60)

    # Nota: number_input ya devuelve un número, pero mantengo tu estructura de lógica
    numero_input = st.number_input("Ingrese un número entero no negativo:", min_value=0, step=1, format="%d")

    if st.button("Calcular Factoriales"):
        try:
            numero = int(numero_input) # Casting explícito como en tu código
            if numero < 0:
                st.error("Error: El factorial solo se puede calcular para números no negativos.")
            else:
                st.write("\n--- 1. Cálculo con bucle 'for' ---")           
                resultado_for = 1
                if numero > 0: 
                    # Tu lógica for original
                    for i in range(1, numero + 1):
                        resultado_for *= i        
                st.write(f"El factorial de {numero}! (usando 'for') es: {resultado_for}")

                st.write("\n--- 2. Cálculo con bucle 'while' ---")        
                resultado_while = 1
                contador = 1
                
                # Tu lógica while original
                while contador <= numero:
                    resultado_while *= contador
                    contador += 1    
                st.write(f"El factorial de {numero}! (usando 'while') es: {resultado_while}")

        except ValueError:
            st.error("\nError: Entrada no válida. Por favor, ingrese un número entero.")
        
        st.text("-" * 60)

# ==========================================
# CÓDIGO 5: TABLA PERIÓDICA
# ==========================================
elif opcion == "5. Tabla Periódica":
    st.header("5_Tabla_periodica")
    st.text("--- Consulta de la Tabla Periódica ---")
    st.text("Busca información de un elemento por su símbolo o número atómico.")
    st.text("-" * 60)

    # Adaptación: En vez de un 'while True' infinito, la web espera el input
    busqueda = st.text_input("Ingrese el símbolo o número atómico a consultar:", placeholder="Ej: H o 1")

    if st.button("Buscar Elemento"):
        if busqueda:
            # Tu lógica de búsqueda original (bucle for sobre la lista)
            elemento_encontrado = None

            for elemento in ELEMENTOS_QUIMICOS:
                if elemento["simbolo"].lower() == busqueda.lower() or str(elemento["numero_atomico"]) == busqueda:
                    elemento_encontrado = elemento
                    break

            st.text("-" * 60)
            if elemento_encontrado:
                st.success(f"Información para el elemento: {elemento_encontrado['nombre']} ({elemento_encontrado['simbolo']})")
                st.write(f"  - Número Atómico: {elemento_encontrado['numero_atomico']}")
                st.write(f"  - Masa Atómica (uma): {elemento_encontrado['masa_atomica']}")
                st.write(f"  - Tipo de Elemento: {elemento_encontrado['tipo']}")
            else:
                st.error(f"Elemento no encontrado. No hay información para '{busqueda}'.")
            st.text("-" * 60)

# ==========================================
# CÓDIGO 6: MRU
# ==========================================
elif opcion == "6. MRU":
    st.header("6_MRU")
    st.text("--- Calculadora de Cinemática (MRU) ---")
    
    # Adaptación: En vez de input("1-4"), usamos un radio button
    menu_mru = st.radio(
        "¿Qué variable deseas calcular?",
        ("1. Distancia (d = v * t)", "2. Velocidad (v = d / t)", "3. Tiempo (t = d / v)")
    )

    if menu_mru == "1. Distancia (d = v * t)":
        v = st.number_input("Ingrese la velocidad (m/s):", value=0.0)
        t = st.number_input("Ingrese el tiempo (s):", value=0.0)
        if st.button("Calcular Distancia"):
            distancia = calcular_distancia(v, t) # Llamada a tu función
            if distancia is not None:
                st.write(f"Resultado: La distancia es {distancia:.2f} metros.")
            else:
                st.error("Error: La velocidad y el tiempo deben ser no negativos.")

    elif menu_mru == "2. Velocidad (v = d / t)":
        d = st.number_input("Ingrese la distancia (metros):", value=0.0)
        t = st.number_input("Ingrese el tiempo (s):", value=0.0)
        if st.button("Calcular Velocidad"):
            velocidad = calcular_velocidad(d, t) # Llamada a tu función
            if velocidad is not None:
                st.write(f"Resultado: La velocidad es {velocidad:.2f} m/s.")
            else:
                st.error("Error: El tiempo debe ser mayor que cero.")

    elif menu_mru == "3. Tiempo (t = d / v)":
        d = st.number_input("Ingrese la distancia (metros):", value=0.0)
        v = st.number_input("Ingrese la velocidad (m/s):", value=0.0)
        if st.button("Calcular Tiempo"):
            tiempo = calcular_tiempo(d, v) # Llamada a tu función
            if tiempo is not None:
                st.write(f"Resultado: El tiempo es {tiempo:.2f} segundos.")
            else:
                st.error("Error: La velocidad debe ser mayor que cero.")
    
    st.text("-" * 40)
