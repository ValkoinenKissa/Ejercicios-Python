# Sistema de Gestión de Reservas – Centro Deportivo (FitLife Center)

Este proyecto es una mini-aplicación en Python orientada a objetos que simula el sistema interno de gestión de reservas de un centro deportivo (FitLife Center S.L.).

Su objetivo es modelar, de forma sencilla pero correcta a nivel de POO, los elementos principales del dominio:

- Usuarios del centro:
  - Clientes
  - Entrenadores
- Actividades:
  - Clases colectivas
  - Entrenamientos personales
- Reservas de actividades
- Cálculo automático de precios y control de plazas

La aplicación está pensada como **fase 1** de un sistema mayor, de cara a futuras ampliaciones (persistencia en base de datos, interfaz gráfica/web, nuevos tipos de usuarios y actividades, etc.).

---

## Estructura del proyecto

```
2025/Actividades_trimestrales/Actividad_trimestral_2/
├── main.py
└── app/
    ├── controller/
    │   ├── app_controller.py
    │   ├── gestor_actividades.py
    │   ├── gestor_reservas.py
    │   └── gestor_usuarios.py
    └── models/
        ├── actividad.py
        ├── clase_colectiva.py
        ├── cliente.py
        ├── empleado.py
        ├── entrenador.py
        ├── entrenamiento_personal.py
        ├── errores.py
        ├── persona.py
        └── reserva.py
```

### Punto de entrada

- **`main.py`**  
  Es el fichero principal del proyecto. Crea una instancia de `AppController` y arranca el bucle principal del menú de la aplicación.

---

## Diseño orientado a objetos

El diseño se basa en **herencia**, **clases abstractas** y **polimorfismo**, cumpliendo los requisitos de POO del enunciado.

### Jerarquía de usuarios

- **`Persona` (`models/persona.py`)**  
  Clase abstracta que representa a cualquier persona del sistema. Define los atributos y métodos comunes:

  - Atributos:
    - `id: str`
    - `nombre: str`
  - Métodos abstractos:
    - `agregar_reserva(self, reserva: Reserva) -> None`
    - `consultar_reservas(self) -> None`

  Esto evita la creación de “usuarios genéricos” y fuerza a definir subclases concretas.

- **`Cliente` (`models/cliente.py`)**  
  Hereda de `Persona` y representa a los clientes del centro:

  - Atributos:
    - `email: str`
    - `reservas: list[Reserva]`
  - Funcionalidad:
    - `consultar_reservas()` → lista por pantalla todas las reservas del cliente, mostrando:
      - Nombre de la actividad
      - Fecha
      - Precio final
      - Ocupación y estado de la actividad
    - `agregar_reserva(reserva)` → asocia una nueva reserva al cliente

- **`Empleado` (`models/empleado.py`)**  
  Clase base sencilla para empleados del centro:

  - Atributos: `id`, `nombre`, `mail`

- **`Entrenador` (`models/entrenador.py`)**  
  Hereda de `Empleado` y representa a los entrenadores del centro:

  - Atributos:
    - `especialidad: str` (yoga, crossfit, musculación, pilates, etc.)
    - `actividades: list[Actividad]` (actividades asignadas)
  - Funcionalidad pensada para futuras ampliaciones:
    - `consultar_actividades_asignadas()`
    - `ver_num_clientes_inscritos()`
    - `ver_ocupacion_total()`

De esta forma, el sistema diferencia claramente entre **Clientes** y **Entrenadores**, sin permitir el uso de una “Persona genérica”.

### Jerarquía de actividades

- **`Actividad` (`models/actividad.py`)**  
  Clase abstracta que define la estructura común de cualquier actividad:

  - Atributos:
    - `nombre: str`
    - `precio_base: float`
    - `plazas_totales: int`
    - `plazas_ocupadas: int = 0`
  - Propiedades:
    - `plazas_disponibles` → plazas libres (totales − ocupadas)
    - `esta_completa` → `True` cuando el aforo se ha llenado
  - Métodos/properties abstractos:
    - `tiene_plazas: bool`
    - `precio_final: float`
    - `control_accesos() -> bool`
    - `reservar_plaza() -> bool`
    - `cancelar_reserva() -> bool`

  Esto obliga a que cada tipo concreto de actividad implemente su propia lógica de precio y de control de aforo.

- **`ClaseColectiva` (`models/clase_colectiva.py`)**  
  Representa actividades grupales (yoga, pilates, spinning, etc.):

  - Atributos adicionales:
    - `horario: str`
  - Lógica:
    - `precio_final` = `precio_base` (no hay recargo)
    - `tiene_plazas` → `plazas_disponibles > 0`
    - `control_accesos` → impide acceso si la actividad está completa
    - `reservar_plaza` → incrementa `plazas_ocupadas` si hay aforo
    - `cancelar_reserva` → libera una plaza si hay reservas

- **`EntrenamientoPersonal` (`models/entrenamiento_personal.py`)**  
  Representa entrenamientos individuales o de grupos muy reducidos:

  - Atributos adicionales:
    - `recargo_porcentaje: float = 20.0`
  - Lógica:
    - `precio_final` = `precio_base * (1 + recargo_porcentaje / 100)`
    - `tiene_plazas`, `control_accesos`, `reservar_plaza`, `cancelar_reserva` adaptados a este tipo de actividad

Gracias a esta jerarquía, el sistema puede tratar las actividades de forma polimórfica a través del tipo `Actividad`, pero aplicando la lógica específica de cada subclase.

### Reservas

- **`Reserva` (`models/reserva.py`)**  
  Clase simple que vincula una actividad y una fecha:

  - Atributos:
    - `actividad: Actividad`
    - `fecha: str`
  - Método:
    - `__str__()` → representación legible de la reserva

Las reservas se almacenan en cada `Cliente` y se usan también para las consultas de información.

---

## Capa de control (controllers)

La lógica de “orquestación” se separa en una capa de control:

### `AppController` (`controller/app_controller.py`)

Es el controlador principal de la aplicación. Gestiona toda la interacción por consola con el usuario:

- Inicialización:
  - Crea instancias de:
    - `GestorUsuarios`
    - `GestorActividades`
    - `GestorReservas` (estructura preparada, aunque la lógica principal está en funciones de módulo)

- Menús:
  - Menú principal:
    - Gestión de Usuarios
    - Gestión de Actividades
    - Gestión de Reservas
    - Consultar información
    - Salir
  - Submenús:
    - Usuarios:
      - Crear cliente
      - Crear entrenador
      - Listar clientes
      - Listar entrenadores
    - Actividades:
      - Crear clase colectiva
      - Crear entrenamiento personal
      - Listar actividades
      - Ver detalles de una actividad
    - Reservas:
      - Realizar reserva
      - Cancelar reserva
      - Ver reservas de un cliente
    - Consultas:
      - Ver reservas de un cliente
      - Ver actividades de un entrenador

- Funciones clave:
  - **Gestión de usuarios**:
    - `crear_cliente()`
    - `crear_entrenador()`
    - `listar_clientes()`
    - `listar_entrenadores()`
  - **Gestión de actividades**:
    - `crear_clase_colectiva()`
    - `crear_entrenamiento_personal()`
    - `listar_actividades()`
    - `ver_detalles_actividad()`
  - **Gestión de reservas**:
    - `realizar_reserva()`
    - `cancelar_reserva()`
    - `ver_reservas_cliente()`
  - **Consultas de entrenadores**:
    - `ver_actividades_entrenador()`

Esta clase centraliza la interacción y delega en los gestores la creación y obtención de datos.

### `GestorUsuarios` (`controller/gestor_usuarios.py`)

Se encarga de gestionar **Clientes** y **Entrenadores**:

- Métodos:
  - `crear_cliente(nombre, email, dni) -> Cliente`
  - `crear_entrenador(nombre, email, especialidad, dni) -> Entrenador`
  - `obtener_clientes() -> list[Cliente]`
  - `obtener_entrenadores() -> list[Entrenador]`
  - `obtener_cliente_por_indice(indice)`
  - `obtener_entrenador_por_indice(indice)`

Mantiene listas internas de clientes y entrenadores, facilitando su acceso desde el controlador.

### `GestorActividades` (`controller/gestor_actividades.py`)

Se responsabiliza de la gestión de actividades:

- Métodos:
  - `crear_clase_colectiva(nombre, precio_base, plazas_totales, horario) -> ClaseColectiva`
  - `crear_entrenamiento_personal(nombre, precio_base, plazas_totales, recargo) -> EntrenamientoPersonal`
  - `obtener_actividades() -> list[Actividad]`
  - `obtener_actividad_por_indice(indice) -> Actividad | None`
- Función auxiliar:
  - `obtener_tipo_actividad(actividad)` → devuelve un string identificando el tipo (Clase Colectiva / Entrenamiento Personal)

### `GestorReservas` (`controller/gestor_reservas.py`)

En este punto, la clase `GestorReservas` está definida pero vacía; la lógica principal de reservas está implementada mediante funciones de módulo:

- `obtener_reservas_cliente(cliente: Cliente) -> list[Reserva]`
- `cancelar_reserva(cliente: Cliente, indice_reserva: int) -> bool`
- `realizar_reserva(cliente: Cliente, actividad: Actividad, fecha: str) -> bool`

Estas funciones:

- Verifican si hay plazas disponibles (`actividad.tiene_plazas`).
- En caso contrario, lanzan la excepción `SinPlazasDisponiblesError`.
- Reservan plaza incrementando `plazas_ocupadas` a través de `actividad.reservar_plaza()`.
- Asocian la reserva al cliente utilizando `cliente.agregar_reserva()`.

---

## Manejo de errores y robustez

El sistema controla situaciones de error principalmente en dos áreas:

1. **Reservas sin plazas disponibles**  
   - Se define la excepción `SinPlazasDisponiblesError` en `models/errores.py`.
   - Se lanza desde `realizar_reserva` cuando `actividad.tiene_plazas` es `False`.
   - Se captura en `AppController.realizar_reserva()` para informar al usuario de manera clara.

2. **Uso de clases abstractas**  
   - `Persona` y `Actividad` están definidas como clases abstractas utilizando `ABC` y `@abstractmethod`.  
   - Python impide su instanciación directa, garantizando que solo se utilicen subclases concretas (Cliente, ClaseColectiva, etc.).

---

## Requisitos del enunciado cubiertos

De forma resumida, este mini-proyecto cubre:

- **RF1 – Gestión de usuarios**  
  Creación y gestión de `Cliente` y `Entrenador`, sin permitir una “Persona” genérica.
- **RF2 – Gestión de actividades**  
  Definición de una estructura común (`Actividad`) y tipos concretos con lógica propia.
- **RF3 – Gestión de reservas**  
  Un cliente puede reservar una actividad, se aplican controles de plazas y se asocian reservas al cliente.
- **RF4 – Cálculo de precios**  
  El precio final se calcula automáticamente según el tipo de actividad, sin intervención del cliente.
- **RF5 – Consulta de información**  
  Los clientes pueden consultar todas sus reservas, visualizando nombre, precio final y estado de ocupación.
- **RF6 – Robustez**  
  Manejo de reservas sin plazas disponibles mediante excepciones, y uso correcto de clases abstractas.

A nivel técnico:

- Proyecto dividido en múltiples ficheros `.py`.
- `main.py` como punto de entrada.
- Uso de:
  - Abstracción (`Persona`, `Actividad`)
  - Herencia (`Cliente`, `Entrenador`, `ClaseColectiva`, `EntrenamientoPersonal`)
  - Polimorfismo (métodos compartidos con implementaciones distintas)
  - Encapsulamiento lógico del estado a través de métodos y propiedades.

---

## Cómo ejecutar el proyecto

1. Asegúrate de estar en la carpeta del proyecto donde se encuentra `main.py`.
2. Ejecuta:

```bash
python main.py
```

3. Navega por los menús:
   - Crea clientes y entrenadores.
   - Crea actividades (clases colectivas o entrenamientos personales).
   - Realiza reservas, cancela y consulta información.

---

## Posibles mejoras futuras

Este proyecto está preparado para ampliaciones como:

- Persistencia de datos en base de datos o ficheros.
- Interfaz gráfica (GUI) o aplicación web.
- Nuevos tipos de usuarios (por ejemplo, administradores) y actividades.
- Implementar completamente la clase `GestorReservas` con métodos de instancia.
- Tests unitarios para validar la lógica de negocio.
