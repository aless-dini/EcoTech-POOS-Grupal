from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamento

proyecto = Proyecto(
    nombre="Aplicación de estacionamientos en tiempo real",
    asignarEmpleado="Alessandro Dini"
)

empleado = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
)

empleado2 = Empleado(
    nombre="Juan Torres",
    correo="ana.torres@ecotech.cl"
)

depto = Departamento(
    nombre="Recursos humanos"
)
