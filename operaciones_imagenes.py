# -*- coding: utf-8 -*-
"""
Realiza operaciones aritméticas y lógicas entre dos imágenes usando OpenCV.

Este script carga dos imágenes ('original.jpg' y 'original2.jpg'),
se asegura de que tengan las mismas dimensiones y luego aplica una serie de
operaciones con OpenCV (suma, resta, AND, OR, etc.).

Dependencias:
    - opencv-python
    - numpy

Uso:
    1. Guarda este script en una carpeta.
    2. Coloca las dos imágenes de entrada ('original.jpg' y 'original2.jpg')
       en la misma carpeta.
    3. Ejecuta el script. Los resultados se guardarán en una nueva
       subcarpeta llamada 'resultados/'.
"""

import cv2
import os

# --- CONFIGURACIÓN ---
# Usar rutas relativas para portabilidad.
# Las imágenes de entrada deben estar en la misma carpeta que el script.
IMAGEN1_PATH = 'original.jpg'
IMAGEN2_PATH = 'original2.jpg'
OUTPUT_FOLDER = 'resultados'

# --- LÓGICA DEL SCRIPT ---
# Crear la carpeta de salida si no existe.
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Carpeta creada en: {OUTPUT_FOLDER}")

# Verificar si las imágenes de entrada existen antes de continuar.
if not os.path.isfile(IMAGEN1_PATH):
    print(f"Error: No se puede encontrar la imagen en '{IMAGEN1_PATH}'")
    exit()
if not os.path.isfile(IMAGEN2_PATH):
    print(f"Error: No se puede encontrar la imagen en '{IMAGEN2_PATH}'")
    exit()

# Cargar las imágenes desde los archivos.
imagen1 = cv2.imread(IMAGEN1_PATH)
imagen2 = cv2.imread(IMAGEN2_PATH)

# Verificar si las imágenes se cargaron correctamente.
if imagen1 is None or imagen2 is None:
    print("Error: No se pudo cargar una o ambas imágenes. Verifica los archivos.")
    exit()

# Asegurarse de que ambas imágenes tengan el mismo tamaño para poder operar.
# Se redimensiona la imagen 1 para que coincida con las dimensiones de la imagen 2.
if imagen1.shape != imagen2.shape:
    print("Las imágenes tienen diferentes tamaños. Redimensionando imagen 1...")
    imagen1 = cv2.resize(imagen1, (imagen2.shape[1], imagen2.shape[0]))

def guardar_y_mostrar(nombre_operacion, imagen_resultado):
    """
    Guarda y muestra una imagen resultante.

    Args:
        nombre_operacion (str): El nombre de la operación (ej. 'suma').
                                Se usará para el nombre del archivo.
        imagen_resultado (numpy.ndarray): La imagen procesada para guardar y mostrar.
    """
    # Construir la ruta completa para guardar la imagen.
    nombre_archivo = f"{nombre_operacion}.jpg"
    save_path = os.path.join(OUTPUT_FOLDER, nombre_archivo)

    # Guardar la imagen en el disco.
    cv2.imwrite(save_path, imagen_resultado)
    print(f"Imagen '{nombre_archivo}' guardada exitosamente en '{OUTPUT_FOLDER}/'")
    
    # Mostrar la imagen en una ventana.
    cv2.imshow(f'Resultado - {nombre_operacion.title()}', imagen_resultado)


# --- REALIZAR OPERACIONES Y MOSTRAR RESULTADOS ---
print("\nRealizando operaciones con imágenes...")

# Operaciones Aritméticas
guardar_y_mostrar('suma', cv2.add(imagen1, imagen2))
guardar_y_mostrar('resta', cv2.subtract(imagen1, imagen2))
guardar_y_mostrar('multiplicacion', cv2.multiply(imagen1, imagen2))
guardar_y_mostrar('division', cv2.divide(imagen1, imagen2))

# Operaciones Lógicas (Bitwise)
guardar_y_mostrar('bitwise_and', cv2.bitwise_and(imagen1, imagen2))
guardar_y_mostrar('bitwise_or', cv2.bitwise_or(imagen1, imagen2))
guardar_y_mostrar('bitwise_xor', cv2.bitwise_xor(imagen1, imagen2))
guardar_y_mostrar('bitwise_not_1', cv2.bitwise_not(imagen1))
guardar_y_mostrar('bitwise_not_2', cv2.bitwise_not(imagen2))

# Esperar a que el usuario presione una tecla para cerrar todas las ventanas.
print("\nOperaciones completadas. Presiona cualquier tecla para cerrar las ventanas.")
cv2.waitKey(0)
cv2.destroyAllWindows()