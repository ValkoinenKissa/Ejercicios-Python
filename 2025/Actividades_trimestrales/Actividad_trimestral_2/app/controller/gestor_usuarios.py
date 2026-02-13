from typing import List
from ..models.cliente import Cliente
from ..models.entrenador import Entrenador


class GestorUsuarios:
    def __init__(self):
        self.clientes: List[Cliente] = []
        self.entrenadores: List[Entrenador] = []

    def crear_cliente(self, nombre: str, email: str, dni: str) -> Cliente:
        cliente = Cliente(id=dni, nombre=nombre, email=email)
        self.clientes.append(cliente)
        return cliente

    def crear_entrenador(self, nombre: str, email: str, especialidad: str, dni:str) -> Entrenador:
        entrenador = Entrenador(nombre=nombre, mail=email, especialidad=especialidad, id=dni)
        self.entrenadores.append(entrenador)
        return entrenador

    def obtener_clientes(self) -> List[Cliente]:
        """Retorna lista de todos los clientes"""
        return self.clientes

    def obtener_entrenadores(self) -> List[Entrenador]:
        """Retorna lista de todos los entrenadores"""
        return self.entrenadores

    def obtener_cliente_por_indice(self, indice: int) -> Cliente | None:
        """Obtiene un cliente por su índice en la lista"""
        if 0 <= indice < len(self.clientes):
            return self.clientes[indice]
        return None

    def obtener_entrenador_por_indice(self, indice: int) -> Entrenador | None:
        """Obtiene un entrenador por su índice en la lista"""
        if 0 <= indice < len(self.entrenadores):
            return self.entrenadores[indice]
        return None