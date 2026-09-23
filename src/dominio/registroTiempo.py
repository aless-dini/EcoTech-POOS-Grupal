class RegistroTiempo:
    def __init__(self, fecha: str, horas: float):
        self.fecha = fecha
        self.horas = horas

    def mostrar_registro(self) -> str:
        return f"{self.fecha} - {self.horas}"

        