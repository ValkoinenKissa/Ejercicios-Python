from dataclasses import dataclass, field

from actividad import Actividad
from empleado import Empleado

@dataclass
class Entrenador(Empleado): # Heredar de la dataclass de empleado
    especialidad: str
    actividades : list[Actividad] = field(default_factory=list)


    def consultar_actividades_asignadas(self) -> None:
        if not self.actividades:
            print("Este entrenador no tiene actividades asignadas")

        else:
            print(f"\nActividades de {self.nombre}:")
            for actividad in self.actividades:
                print(f"- {actividad}")

    def ver_num_clientes_inscritos(self) -> None:
        if not self.actividades:
            print("Este entrenador no tiene actividades asignadas")
        else:
            print(f"\nResumen de inscripciones - {self.nombre}:")
            for actividad in self.actividades:
                print(f"- {actividad.nombre}: {actividad.plazas_ocupadas}/{actividad.plazas_totales} inscritos "
                      f"({actividad.plazas_disponibles} plazas disponibles)")


    def ver_ocupacion_total(self) -> None:
        if not self.actividades:
            print(f"{self.nombre} no tiene actividades asignadas")
            return

        total_plazas = sum(act.plazas_totales for act in self.actividades)
        total_ocupadas = sum(act.plazas_ocupadas for act in self.actividades)

        print(f"\nOcupación total de {self.nombre}:")
        print(f"Total de plazas: {total_plazas}")
        print(f"Plazas ocupadas: {total_ocupadas}")
        print(f"Plazas disponibles: {total_plazas - total_ocupadas}")

        if total_plazas > 0:
            print(f"Porcentaje de ocupación: {(total_ocupadas / total_plazas) * 100:.1f}%")
        else:
            print("Porcentaje de ocupación: 0.0%")