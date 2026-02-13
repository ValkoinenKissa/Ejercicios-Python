from dataclasses import dataclass, field
from .persona import Persona
from .reserva import Reserva

@dataclass
class Cliente(Persona):
    email: str
    reservas: list[Reserva] = field(default_factory=list)

    def consultar_reservas(self) -> None:
        if not self.reservas:
            print(f"\n{self.nombre} no tiene reservas")
            return

        print(f"\n--- RESERVAS DE {self.nombre} ---")
        for i, reserva in enumerate(self.reservas, 1):
            print(f"\n{i}. Actividad: {reserva.actividad.nombre}")
            print(f"   Fecha: {reserva.fecha}")
            print(f"   Precio final: {reserva.actividad.precio_final:.2f}€")
            print(f"   Ocupación: {reserva.actividad.plazas_ocupadas}/{reserva.actividad.plazas_totales}")
            print(f"   Estado: {'COMPLETA' if reserva.actividad.esta_completa else f'{reserva.actividad.plazas_disponibles} plazas disponibles'}")

    def agregar_reserva(self, reserva: Reserva) -> None:
        self.reservas.append(reserva)