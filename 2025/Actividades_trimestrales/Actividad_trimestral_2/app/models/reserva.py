from dataclasses import dataclass
from .actividad import Actividad

@dataclass
class Reserva:
    actividad: Actividad
    fecha: str

    def __str__(self) -> str:
        return f"Reserva: {self.actividad.nombre} el {self.fecha}"

