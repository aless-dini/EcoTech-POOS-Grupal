from dominio.registroTiempo import RegistroTiempo
from dominio.proyecto import Proyecto

class Empleado:
    def __init__(self, nombre: str, direccion: str, numeracion: int, telefono: int, correo: str, salario: float, inicioContrato: str,  id = None):
        self.id = id,
        self.nombre = nombre,
        self.direccion = direccion,
        self.numeracion = numeracion,
        self.telefono = numero,
        self.correo = correo
        self.salario = salario,
        self.inicioContrato = inicioContrato

    def __str__(self):
        print(f"Nombre: {self.nombre}, Correo: {self.correo}")



        