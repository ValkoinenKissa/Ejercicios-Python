from .gestor_usuarios import GestorUsuarios
from .gestor_actividades import GestorActividades, obtener_tipo_actividad
from .gestor_reservas import GestorReservas, obtener_reservas_cliente, cancelar_reserva
from ..models.clase_colectiva import ClaseColectiva
from ..models.entrenamiento_personal import EntrenamientoPersonal


def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN - CENTRO DEPORTIVO")
    print("=" * 50)
    print("1. Gestión de Usuarios")
    print("2. Gestión de Actividades")
    print("3. Gestión de Reservas")
    print("4. Consultar Información")
    print("5. Salir")
    print("=" * 50)


def mostrar_menu_usuarios():
    print("\n--- GESTIÓN DE USUARIOS ---")
    print("1. Crear Cliente")
    print("2. Crear Entrenador")
    print("3. Listar Clientes")
    print("4. Listar Entrenadores")
    print("5. Volver")


def mostrar_menu_actividades():
    print("\n--- GESTIÓN DE ACTIVIDADES ---")
    print("1. Crear Clase Colectiva")
    print("2. Crear Entrenamiento Personal")
    print("3. Listar Actividades")
    print("4. Ver Detalles de Actividad")
    print("5. Volver")


def mostrar_menu_reservas():
    print("\n--- GESTIÓN DE RESERVAS ---")
    print("1. Realizar Reserva")
    print("2. Cancelar Reserva")
    print("3. Ver Reservas de un Cliente")
    print("4. Volver")


class AppController:
    def __init__(self):
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_actividades = GestorActividades()
        self.gestor_reservas = GestorReservas()

    # --- Gestión de Usuarios ---

    def crear_cliente(self):
        print("\n--- CREAR CLIENTE ---")
        nombre = input("Nombre: ")
        email = input("Email: ")
        dni = input("DNI: ")

        cliente = self.gestor_usuarios.crear_cliente(nombre, email, dni)
        print(f"✅ Cliente '{cliente.nombre}' creado correctamente")

    def crear_entrenador(self):
        print("\n--- CREAR ENTRENADOR ---")
        nombre = input("Nombre: ")
        email = input("Email: ")
        especialidad = input("Especialidad (yoga/crossfit/musculación/pilates): ")
        dni = input("Introduce el DNI del entrenador: ")

        entrenador = self.gestor_usuarios.crear_entrenador(nombre, email, especialidad, dni)
        print(f"✅ Entrenador '{entrenador.nombre}' creado correctamente")

    def listar_clientes(self):
        print("\n--- LISTADO DE CLIENTES ---")
        clientes = self.gestor_usuarios.obtener_clientes()

        if not clientes:
            print("No hay clientes registrados")
            return

        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente.nombre} - {cliente.email} (DNI: {cliente.id})")

    def listar_entrenadores(self):
        print("\n--- LISTADO DE ENTRENADORES ---")
        entrenadores = self.gestor_usuarios.obtener_entrenadores()

        if not entrenadores:
            print("No hay entrenadores registrados")
            return

        for i, entrenador in enumerate(entrenadores, 1):
            print(f"{i}. {entrenador.nombre} - {entrenador.especialidad}")

    # --- Gestión de Actividades ---

    def crear_clase_colectiva(self):
        print("\n--- CREAR CLASE COLECTIVA ---")
        nombre = input("Nombre de la clase: ")
        precio_base = float(input("Precio base (€): "))
        plazas_totales = int(input("Plazas totales: "))
        horario = input("Horario: ")

        clase = self.gestor_actividades.crear_clase_colectiva(
            nombre, precio_base, plazas_totales, horario
        )
        print(f"✅ Clase colectiva '{clase.nombre}' creada correctamente")

    def crear_entrenamiento_personal(self):
        print("\n--- CREAR ENTRENAMIENTO PERSONAL ---")
        nombre = input("Nombre del entrenamiento: ")
        precio_base = float(input("Precio base (€): "))
        plazas_totales = int(input("Plazas totales (normalmente 1-2): "))
        recargo = float(input("Recargo porcentual (ej: 20 para 20%): "))

        entrenamiento = self.gestor_actividades.crear_entrenamiento_personal(
            nombre, precio_base, plazas_totales, recargo
        )
        print(f"✅ Entrenamiento personal '{entrenamiento.nombre}' creado correctamente")

    def listar_actividades(self):
        print("\n--- LISTADO DE ACTIVIDADES ---")
        actividades = self.gestor_actividades.obtener_actividades()

        if not actividades:
            print("No hay actividades registradas")
            return

        for i, actividad in enumerate(actividades, 1):
            tipo = obtener_tipo_actividad(actividad)
            print(f"{i}. [{tipo}] {actividad.nombre}")
            print(f"   Precio final: {actividad.precio_final:.2f}€")
            print(f"   Plazas: {actividad.plazas_ocupadas}/{actividad.plazas_totales}")
            print(f"   Disponibles: {actividad.plazas_disponibles}")

    def ver_detalles_actividad(self):
        self.listar_actividades()
        actividades = self.gestor_actividades.obtener_actividades()

        if not actividades:
            return

        try:
            num = int(input("\nNúmero de actividad a ver: "))
            actividad = self.gestor_actividades.obtener_actividad_por_indice(num - 1)

            if actividad:
                print(f"\n--- DETALLES: {actividad.nombre} ---")
                print(f"Precio base: {actividad.precio_base:.2f}€")
                print(f"Precio final: {actividad.precio_final:.2f}€")
                print(f"Plazas totales: {actividad.plazas_totales}")
                print(f"Plazas ocupadas: {actividad.plazas_ocupadas}")
                print(f"Plazas disponibles: {actividad.plazas_disponibles}")
                print(f"¿Tiene plazas?: {'Sí' if actividad.tiene_plazas else 'No'}")
                print(f"¿Está completa?: {'Sí' if actividad.esta_completa else 'No'}")

                if isinstance(actividad, ClaseColectiva):
                    print(f"Horario: {actividad.horario}")
                elif isinstance(actividad, EntrenamientoPersonal):
                    print(f"Recargo: {actividad.recargo_porcentaje}%")
            else:
                print("❌ Número inválido")
        except ValueError:
            print("❌ Entrada inválida")

    # --- Gestión de Reservas ---

    def realizar_reserva(self):
        print("\n--- REALIZAR RESERVA ---")

        # Mostrar y seleccionar cliente
        self.listar_clientes()
        clientes = self.gestor_usuarios.obtener_clientes()

        if not clientes:
            return

        try:
            num_cliente = int(input("\nSeleccione número de cliente: "))
            cliente = self.gestor_usuarios.obtener_cliente_por_indice(num_cliente - 1)

            if not cliente:
                print("❌ Cliente inválido")
                return

            # Mostrar y seleccionar actividad
            self.listar_actividades()
            actividades = self.gestor_actividades.obtener_actividades()

            if not actividades:
                return

            num_actividad = int(input("\nSeleccione número de actividad: "))
            actividad = self.gestor_actividades.obtener_actividad_por_indice(num_actividad - 1)

            if not actividad:
                print("❌ Actividad inválida")
                return

            # Verificar disponibilidad
            if not actividad.tiene_plazas:
                print(f"❌ No hay plazas disponibles en '{actividad.nombre}'")
                return

            # Pedir fecha
            fecha = input("Fecha de la reserva (ej: 2024-03-15): ")

            # Realizar reserva a través del gestor
            if self.gestor_reservas.realizar_reserva(cliente, actividad, fecha):
                print(f"\n✅ RESERVA CONFIRMADA")
                print(f"Cliente: {cliente.nombre}")
                print(f"Actividad: {actividad.nombre}")
                print(f"Precio final: {actividad.precio_final:.2f}€")
                print(f"Fecha: {fecha}")
            else:
                print("❌ No se pudo realizar la reserva")

        except ValueError:
            print("❌ Entrada inválida")

    def cancelar_reserva(self):
        print("\n--- CANCELAR RESERVA ---")

        self.listar_clientes()
        clientes = self.gestor_usuarios.obtener_clientes()

        if not clientes:
            return

        try:
            num_cliente = int(input("\nSeleccione número de cliente: "))
            cliente = self.gestor_usuarios.obtener_cliente_por_indice(num_cliente - 1)

            if not cliente:
                print("❌ Cliente inválido")
                return

            # Mostrar reservas del cliente
            reservas = obtener_reservas_cliente(cliente)

            if not reservas:
                print(f"El cliente {cliente.nombre} no tiene reservas")
                return

            print(f"\nReservas de {cliente.nombre}:")
            for i, reserva in enumerate(reservas, 1):
                print(f"{i}. {reserva.actividad.nombre} - {reserva.fecha}")

            num_reserva = int(input("\nSeleccione número de reserva a cancelar: "))

            if cancelar_reserva(cliente, num_reserva - 1):
                print(f"✅ Reserva cancelada correctamente")
            else:
                print("❌ No se pudo cancelar la reserva")

        except ValueError:
            print("❌ Entrada inválida")

    def ver_reservas_cliente(self):
        print("\n--- CONSULTAR RESERVAS ---")

        self.listar_clientes()
        clientes = self.gestor_usuarios.obtener_clientes()

        if not clientes:
            return

        try:
            num_cliente = int(input("\nSeleccione número de cliente: "))
            cliente = self.gestor_usuarios.obtener_cliente_por_indice(num_cliente - 1)

            if cliente:
                cliente.consultar_reservas()  # RF5
            else:
                print("❌ Cliente inválido")

        except ValueError:
            print("❌ Entrada inválida")

    def ver_actividades_entrenador(self):
        self.listar_entrenadores()
        entrenadores = self.gestor_usuarios.obtener_entrenadores()

        if not entrenadores:
            return

        try:
            num = int(input("\nNúmero de entrenador: "))
            entrenador = self.gestor_usuarios.obtener_entrenador_por_indice(num - 1)

            if entrenador:
                entrenador.consultar_actividades_asignadas()
            else:
                print("❌ Entrenador inválido")
        except ValueError:
            print("❌ Entrada inválida")

    # --- Bucle principal ---

    def ejecutar(self):
        while True:
            mostrar_menu_principal()
            opcion = input("\nSeleccione una opción: ")

            match opcion:
                case "1":  # Gestión de Usuarios
                    self.menu_usuarios()

                case "2":  # Gestión de Actividades
                    self.menu_actividades()

                case "3":  # Gestión de Reservas
                    self.menu_reservas()

                case "4":  # Consultar Información
                    self.menu_consultas()

                case "5":  # Salir
                    print("\n👋 ¡Hasta luego!")
                    break

                case _:
                    print("❌ Opción inválida. Intente de nuevo.")

    def menu_usuarios(self):
        while True:
            mostrar_menu_usuarios()
            sub_opcion = input("\nSeleccione una opción: ")

            match sub_opcion:
                case "1":
                    self.crear_cliente()
                case "2":
                    self.crear_entrenador()
                case "3":
                    self.listar_clientes()
                case "4":
                    self.listar_entrenadores()
                case "5":
                    break
                case _:
                    print("❌ Opción inválida")

    def menu_actividades(self):
        while True:
            mostrar_menu_actividades()
            sub_opcion = input("\nSeleccione una opción: ")

            match sub_opcion:
                case "1":
                    self.crear_clase_colectiva()
                case "2":
                    self.crear_entrenamiento_personal()
                case "3":
                    self.listar_actividades()
                case "4":
                    self.ver_detalles_actividad()
                case "5":
                    break
                case _:
                    print("❌ Opción inválida")

    def menu_reservas(self):
        while True:
            mostrar_menu_reservas()
            sub_opcion = input("\nSeleccione una opción: ")

            match sub_opcion:
                case "1":
                    self.realizar_reserva()
                case "2":
                    self.cancelar_reserva()
                case "3":
                    self.ver_reservas_cliente()
                case "4":
                    break
                case _:
                    print("❌ Opción inválida")

    def menu_consultas(self):
        print("\n--- CONSULTAR INFORMACIÓN ---")
        print("1. Ver reservas de un cliente")
        print("2. Ver actividades de un entrenador")
        sub_opcion = input("\nSeleccione una opción: ")

        match sub_opcion:
            case "1":
                self.ver_reservas_cliente()
            case "2":
                self.ver_actividades_entrenador()
            case _:
                print("❌ Opción inválida")