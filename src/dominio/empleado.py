from dominio.registroTiempo import RegistroTiempo

class Empleado:
    def __init__(self, nombre: str, direccion: str, numeracion: int, numero: int, correo: str, salario: float, inicioContrato: str, id=None):
        self.id = id,
        self.nombre = nombre,
        self.direccion = direccion,
        self.numeracion = numeracion,
        self.numero = numero,
        self.correo = correo
        self.salario = salario,
        self.inicioContrato = inicioContrato
        self._registro_tiempo:list[RegistroTiempo] = []

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo}"

    def registrar_tiempo(self, rg:RegistroTiempo) -> bool:
        if rg in self._registro_tiempo:
            return False
    
        self._registro_tiempo.append(rg)
        return True






        