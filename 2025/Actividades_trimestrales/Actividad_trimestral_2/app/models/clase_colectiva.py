from dataclasses import dataclass
from .actividad import Actividad


@dataclass
class ClaseColectiva(Actividad):
    horario: str = ""


    @property
    def tiene_plazas(self) -> bool:
        return self.plazas_disponibles > 0

    @property
    def precio_final(self) -> float:
        return self.precio_base

    def control_accesos(self) -> bool:
        if self.esta_completa:
            print(f" {self.nombre} - Aforo completo ({self.plazas_ocupadas}/{self.plazas_totales})")
            return False
        return True

    def reservar_plaza(self) -> bool:
        if not self.control_accesos():
            return False

        self.plazas_ocupadas += 1
        print(f" Plaza reservada en {self.nombre}")
        print(f"   Quedan {self.plazas_disponibles} plazas disponibles")
        return True

    def cancelar_reserva(self) -> bool:
        if self.plazas_ocupadas == 0:
            print("No hay reservas para cancelar")
            return False

        self.plazas_ocupadas -= 1
        print(f"Reserva cancelada. Ahora hay {self.plazas_disponibles} plazas disponibles")
        return True