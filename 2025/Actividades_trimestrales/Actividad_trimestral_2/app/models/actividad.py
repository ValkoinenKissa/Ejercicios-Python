from dataclasses import dataclass


@dataclass
class Actividad:
    nombre: str
    plazas_totales: int
    plazas_ocupadas: int = 0

    @property
    def plazas_disponibles(self) -> int:
        return self.plazas_totales - self.plazas_ocupadas

    @property
    def tiene_plazas(self) -> bool:
        return self.plazas_disponibles > 0