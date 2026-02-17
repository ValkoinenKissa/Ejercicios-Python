from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class Actividad(ABC): # Declaración como clase abstracta
    nombre: str
    precio_base: float
    plazas_totales: int
    plazas_ocupadas: int = 0


    @property
    def plazas_disponibles(self) -> int:
        return self.plazas_totales - self.plazas_ocupadas

    @property
    def esta_completa(self) -> bool:
        """Indica si la actividad ha alcanzado el aforo máximo."""
        return self.plazas_disponibles == 0

    @property
    @abstractmethod
    def tiene_plazas(self) -> bool:
        pass
    @property
    @abstractmethod
    def precio_final(self) -> float:
        pass

    @abstractmethod
    def control_accesos(self) -> bool:
        pass

    @abstractmethod
    def reservar_plaza(self) -> bool:
       pass

    @abstractmethod
    def cancelar_reserva(self) -> bool:
        pass