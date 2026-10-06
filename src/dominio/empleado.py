from datetime import date, datetime
 
 
class Empleado:
    """Entidad Empleado: solo datos y validaciones propias (sin acceso a BD)."""
 
    def __init__(self, id=None, nombre=None, direccion=None, numeracion=None,
                 telefono=None, correo=None, salario=None, inicioContrato=None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.numeracion = numeracion
        self.telefono = telefono
        self.correo = correo
        self.salario = salario
        self.inicioContrato = inicioContrato  # formato "YYYY-MM-DD"
 
    # ---------- Validaciones ----------
    def validarCorreo(self):
        """Valida de forma básica que el correo tenga formato nombre@dominio.ext"""
        try:
            correo = self.correo.strip()
            if " " in correo or correo.count("@") != 1:
                return False
            local, dominio = correo.split("@")
            return (bool(local) and "." in dominio
                    and not dominio.startswith(".") and not dominio.endswith("."))
        except AttributeError:
            # correo es None o no es texto
            return False
        except Exception as e:
            print(f"Error al validar el correo: {e}")
            return False
 
    def validarSalario(self):
        """El salario debe ser un entero mayor que 0."""
        try:
            return (isinstance(self.salario, int)
                    and not isinstance(self.salario, bool)
                    and self.salario > 0)
        except Exception as e:
            print(f"Error al validar el salario: {e}")
            return False
 
    # ---------- Cálculos ----------
    def calcularAntiguedad(self):
        """Devuelve los años completos desde inicioContrato hasta hoy.
        Si la fecha no existe o tiene mal formato, devuelve 0."""
        try:
            if not self.inicioContrato:
                return 0
            inicio = datetime.strptime(str(self.inicioContrato), "%Y-%m-%d").date()
            hoy = date.today()
            anios = hoy.year - inicio.year
            if (hoy.month, hoy.day) < (inicio.month, inicio.day):
                anios -= 1
            return max(anios, 0)
        except ValueError:
            print("Error: inicioContrato debe tener formato AAAA-MM-DD")
            return 0
        except Exception as e:
            print(f"Error al calcular la antigüedad: {e}")
            return 0
 
    # ---------- Representación ----------
    def __str__(self):
        return (f"Empleado(id={self.id}, nombre={self.nombre}, correo={self.correo}, "
                f"telefono={self.telefono}, salario={self.salario}, "
                f"inicioContrato={self.inicioContrato})")






        