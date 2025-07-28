5. Consulta de la Tabla Periódica

Este script (`tabla_periodica.py`) funciona como una base de datos interactiva que permite al usuario consultar información sobre los elementos químicos de la tabla periódica.

La implementación se basa en:
*   Una **lista** principal que actúa como el contenedor para los 118 elementos químicos.
*   **Diccionarios** anidados dentro de la lista, donde cada diccionario representa un elemento y almacena sus propiedades (símbolo, nombre, masa atómica, etc.) con claves descriptivas.

El programa permite al usuario buscar un elemento por su **símbolo** o por su **número atómico**. Recorre la estructura de datos, busca una coincidencia y presenta la información de manera ordenada. Este enfoque muestra cómo las listas y los diccionarios trabajan juntos para crear una estructura de datos flexible, escalable y potente.