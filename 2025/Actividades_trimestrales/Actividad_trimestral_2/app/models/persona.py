from abc import ABC, abstractmethod
from dataclasses import dataclass

from .reserva import Reserva
@dataclass
class Persona(ABC):
    id:str
    nombre: str

    @abstractmethod
    def agregar_reserva(self, reserva: Reserva) -> None:
        pass

    @abstractmethod
    def consultar_reservas(self) -> None:
        pass