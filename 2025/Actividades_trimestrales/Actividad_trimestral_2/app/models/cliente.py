from dataclasses import dataclass, field
from typing import Optional

from reserva import Reserva
from actividad import Actividad
@dataclass
class Persona:
    nombre: str
    email: str
    reservas: list[Reserva] = field(default_factory=list)
    actividades: list[Actividad] = field(default_factory=list)

    def consultar_reservas(self) -> None:
        if not self.reservas:
            print("No tiene reservas")
            return
        for reserva in self.reservas:
            print(reserva)

    def reservar(self, actividad: Actividad, fecha:str) -> Optional[Reserva]:
        if not actividad.tiene_plazas:
            print(f"No hay plazas disponibles en '{actividad.nombre}'")
            return None

        reserva = Reserva(actividad=actividad, fecha=fecha)
        self.reservas.append(reserva)
        self.actividades.append(actividad)
        actividad.plazas_ocupadas += 1

        print(f"Reserva realizada: {actividad.nombre} el {fecha}")
        return reserva