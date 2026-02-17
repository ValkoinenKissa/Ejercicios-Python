from dataclasses import dataclass
from .actividad import Actividad


@dataclass
class EntrenamientoPersonal(Actividad):
    """Entrenamientos personalizados con recargo adicional"""
    recargo_porcentaje: float = 20.0  # 20% de recargo por defecto

    @property
    def tiene_plazas(self) -> bool:
        return self.plazas_disponibles > 0

    @property
    def precio_final(self) -> float:
        """Precio base + recargo porcentual"""
        return self.precio_base * (1 + self.recargo_porcentaje / 100)

    def control_accesos(self) -> bool:
        """Verifica si se puede realizar una reserva"""
        if self.esta_completa:
            print(f" {self.nombre} - Aforo completo ({self.plazas_ocupadas}/{self.plazas_totales})")
            return False
        return True

    def reservar_plaza(self) -> bool:
        """Intenta reservar una plaza"""
        if not self.control_accesos():
            return False

        self.plazas_ocupadas += 1
        print(f"Plaza reservada en {self.nombre}")
        print(f"   Quedan {self.plazas_disponibles} plazas disponibles")
        print(f"   Precio: {self.precio_final:.2f}€")
        return True

    def cancelar_reserva(self) -> bool:
        """Cancela una reserva existente"""
        if self.plazas_ocupadas == 0:
            print("No hay reservas para cancelar")
            return False

        self.plazas_ocupadas -= 1
        print(f"Reserva cancelada. Ahora hay {self.plazas_disponibles} plazas disponibles")
        return True