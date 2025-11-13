# Gestión de inventario — Decisión de diseño y guía de corrección

Este proyecto implementa el ejercicio de "Gestión de inventario de una tienda electrónica" utilizando el patrón de diseño MVC (Model–View–Controller) para mejorar separación de responsabilidades, legibilidad y escalabilidad, tal y como se haría en un proyecto real.

Para cumplir literalmente con el requisito de entrega, se incluye un archivo `gestion_inventario.py` que actúa como punto de entrada y arranca la aplicación manteniendo la arquitectura modular.

## Estructura del proyecto

```
2025/Actividad_trimestral/
├─ gestion_inventario.py     # Punto de entrada al programa; delega en Controller
├─ app_controller.py             # Controller: orquesta las acciones del usuario
├─ io_ops.py                 # I/O: lectura/escritura de inventario y utilidades
├─ product.py                # Modelo de dominio: Product (nombre, precio, stock)
└─ data/
   └─ inventario.txt         # Persistencia del inventario (se crea si no existe)
```

Nota: el inventario se guarda en `data/inventario.txt`. Si el profesor espera exactamente `inventario.txt` en la raíz, se puede ajustar la ruta fácilmente; en esta entrega se documenta y se versiona en `data/`.

## Cómo ejecutar

Requisitos: Python 3.10+ (se usa `match/case`).

Desde la carpeta `2025/Actividad_trimestral`:

```bash
python gestion_inventario.py
```

El programa mostrará un menú con las opciones solicitadas.

## Cumplimiento de requisitos del enunciado

- Carga del Inventario: ✅
  - Se lee desde `data/inventario.txt`. Si no existe, se crea automáticamente con datos de ejemplo.
- Mostrar el Inventario: ✅
  - Opción del menú dedicada a imprimir nombre, precio y cantidad de cada producto en formato legible.
- Calcular el Valor Total del Inventario: ✅
  - Se calcula el valor total (precio × cantidad) y se muestra por pantalla.
- Identificar Productos Agotados: ✅
  - Se listan los productos cuya cantidad disponible es 0.
- Actualizar Cantidad de un Producto: ✅
  - El usuario puede seleccionar un producto y modificar su cantidad; el cambio persiste en `inventario.txt`.
- Persistencia: ✅
  - Todas las operaciones de lectura/escritura impactan en el fichero `data/inventario.txt`.

## Funcionalidad extra

- Inserción de nuevos productos en el inventario (opción adicional del menú), incluyendo persistencia en el fichero.

## Decisiones técnicas

- Patrón MVC para separar responsabilidades:
  - `product.py` (Modelo): datos y representación de productos.
  - `app_controller.py` (Controlador): lógica del flujo de datos.
  - `io_ops.py` (Persistencia / View I/O): lectura, escritura y formateo de salida.
- Nomenclatura en inglés en clases/métodos/variables por coherencia con prácticas de proyectos reales.
- Fichero `gestion_inventario.py` para cumplir literalmente el requisito de la tarea sin sacrificar la arquitectura.

## Notas para el corrector

- Si se desea que el inventario resida exactamente en `inventario.txt` en la misma carpeta que el programa, se puede modificar la ruta en `controller.py` (variable `path`) de `data/inventario.txt` a `inventario.txt`. En esta entrega se documenta que está en `data/`.
- Se adjunta `data/inventario.txt` generado por el programa, tal y como pide el enunciado.
