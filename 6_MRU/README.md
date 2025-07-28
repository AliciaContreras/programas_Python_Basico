    6. Calculadora de Cinemática (MRU)

    Este script (calculadora_cinematica.py) es una herramienta interactiva que calcula las variables del Movimiento Rectilíneo Uniforme (distancia, velocidad o tiempo) a partir de las otras dos.

    El programa está estructurado en dos partes principales:

        Funciones de Cálculo: Se definen funciones separadas y reutilizables para cada cálculo (calcular_distancia, calcular_velocidad, calcular_tiempo). Cada función tiene una única responsabilidad, acepta parámetros y retorna un resultado, lo que las hace independientes de la interfaz de usuario.

        Función Principal (Interfaz): Una función iniciar_calculadora maneja el menú interactivo, la entrada del usuario y las llamadas a las funciones de cálculo correspondientes.

    Este diseño separa la lógica de negocio (los cálculos) de la lógica de presentación (el menú), que es un principio fundamental para escribir código limpio, organizado y mantenible.