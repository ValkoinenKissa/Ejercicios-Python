from typing import List
from ..models.actividad import Actividad
from ..models.clase_colectiva import ClaseColectiva
from ..models.entrenamiento_personal import EntrenamientoPersonal


def obtener_tipo_actividad(actividad: Actividad) -> str:
    """Retorna el tipo de actividad como string"""
    if isinstance(actividad, ClaseColectiva):
        return "Clase Colectiva"
    elif isinstance(actividad, EntrenamientoPersonal):
        return "Entrenamiento Personal"
    return "Actividad"


class GestorActividades:
    def __init__(self):
        self.actividades: List[Actividad] = []

    def crear_clase_colectiva(self, nombre: str, precio_base: float,
                              plazas_totales: int, horario: str) -> ClaseColectiva:
        """RF2 - Crear actividad tipo ClaseColectiva"""
        clase = ClaseColectiva(
            nombre=nombre,
            precio_base=precio_base,
            plazas_totales=plazas_totales,
            horario=horario
        )
        self.actividades.append(clase)
        return clase

    def crear_entrenamiento_personal(self, nombre: str, precio_base: float,
                                     plazas_totales: int, recargo: float) -> EntrenamientoPersonal:
        """RF2 - Crear actividad tipo EntrenamientoPersonal"""
        entrenamiento = EntrenamientoPersonal(
            nombre=nombre,
            precio_base=precio_base,
            plazas_totales=plazas_totales,
            recargo_porcentaje=recargo
        )
        self.actividades.append(entrenamiento)
        return entrenamiento

    def obtener_actividades(self) -> List[Actividad]:
        """Retorna lista de todas las actividades"""
        return self.actividades

    def obtener_actividad_por_indice(self, indice: int) -> Actividad | None:
        """Obtiene una actividad por su índice en la lista"""
        if 0 <= indice < len(self.actividades):
            return self.actividades[indice]
        return None

    