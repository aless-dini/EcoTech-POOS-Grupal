class Proyecto :
    def __init__(self, nombre: str, descripcion: str, fechaInicio: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.asignarEmpleado}"

