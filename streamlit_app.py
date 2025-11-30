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
    # ... (He mantenido tu estructura de lista de diccionarios)
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
