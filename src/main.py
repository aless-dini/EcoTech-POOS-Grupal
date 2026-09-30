from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas

try: 
    empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl", direccion="Pasaje Messina", numeracion=418, numero=929734409, salario=1000000, inicioContrato="30/09/2026")
    empleado = EmpleadoDAO.insertar(empleado)
    
    if empleado:
        print("Se agregó correctamente el empleado")
    else:
        print("No se agregó el empleado")

except Exception:
    print("No fue posible completar la operación")





# print(empleado.mostrar_datos())

# empleado.actualizar_nombre("Alex")

# resultado = EmpleadoDAO.actualizar(empleado)

# print(resultado)
