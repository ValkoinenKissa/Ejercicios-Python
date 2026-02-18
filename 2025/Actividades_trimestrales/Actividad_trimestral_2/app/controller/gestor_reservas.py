from typing import List
from ..models.cliente import Cliente
from ..models.actividad import Actividad
from ..models.reserva import Reserva
from ..models.errores import SinPlazasDisponiblesError


def obtener_reservas_cliente(cliente: Cliente) -> List[Reserva]:
    """RF5 - Consulta de información de reservas"""
    return cliente.reservas


def cancelar_reserva(cliente: Cliente, indice_reserva: int) -> bool:
    """Cancela una reserva específica de un cliente"""
    if 0 <= indice_reserva < len(cliente.reservas):
        reserva = cliente.reservas[indice_reserva]

        # Cancelar en la actividad (libera plaza)
        if reserva.actividad.cancelar_reserva():
            cliente.reservas.remove(reserva)
            return True

    return False


def realizar_reserva(cliente: Cliente, actividad: Actividad, fecha: str) -> bool:
    """
    RF3 - Gestión de reservas
    Realiza una reserva verificando disponibilidad
    """
    # RF3 - Comprobar plazas disponibles
    if not actividad.tiene_plazas:
        raise SinPlazasDisponiblesError(
            f"No hay plazas disponibles en la actividad '{actividad.nombre}'"
        )

    # Crear reserva
    reserva = Reserva(actividad=actividad, fecha=fecha)

    # RF3 - Reservar plaza (incrementa plazas_ocupadas)
    if actividad.reservar_plaza():
        cliente.agregar_reserva(reserva)
        return True

    return False


class GestorReservas:
    pass

