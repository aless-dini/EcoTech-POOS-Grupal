from persistencia.empleado_dao import EmpleadoDAO
from dominio.empleado import Empleado

def ingresar_datos():
    nombre = input("\nNombre: ").strip()
    direccion = input("Dirección: ").strip()
    telefono = int(input("Teléfono: "))
    correo = input("Correo: ").strip()
    salario = float(input("Salario: "))
    inicioContrato = input("Inicio contrato: ").strip()
    return nombre, direccion, telefono, correo, salario, inicioContrato

def gestionar_empleados():
    print("1. Registrar empleado")
    print("2. Listar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("6. Salir")

def registrar_empleado():
    nombre, direccion, telefono, correo, salario, inicioContrato = ingresar_datos()

    empleado = Empleado(nombre, direccion, telefono, correo, salario, inicioContrato)
    print(empleado.mostrar_datos())
    try:
        EmpleadoDAO.insertar(empleado)
        print("\nEmpleado registrado correctamente.")

    except Exception:
        print("\nNo fue posible registrar el empleado.")

def eliminar_empleado():
    idEmpleado = input("Ingrese el id del empleado que desea eliminar: ")

    try:
        EmpleadoDAO.eliminar(idEmpleado)
        print("Empleado eliminado correctamente")
    
    except Exception:
        print("\nNo fue posible eliminar al empleado")