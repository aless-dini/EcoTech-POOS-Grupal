from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamento
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.crear_bd import crear_tablas

def menu():
    print("\n*****Bienvenido al programa de Ecotech*****")
    print("1. Gestionar empleados")
    print("2. Gestionar departamentos")
    print("3. Gestionar proyectos")
    print("4. Gestionar registros de tiempo")
    print("5. Gestionar usuarios")
    print("6. Salir")

def registrar_empleado():
    nombre = input("Nombre: ").strip()
    direccion = input("Dirección: ").strip()
    numeracion = int(input("Numeración: ")).strip()
    telefono = int(input("Teléfono: ")).strip()
    correo = input("Correo: ").strip()
    salario = float(input("Salario: ")).strip()
    inicioContrato = input("Inicio contrato: ").strip()

    empleado = Empleado(nombre, direccion, numeracion, telefono, correo, salario, inicioContrato)
    print(empleado.mostrar_datos())
    try:
        EmpleadoDAO.insertar(empleado)
        print("Empleado registrado correctamente.")

    except Exception:
        print("No fue posible registrar el empleado.")


def main():
    while True:
        menu()

        seleccion = input("¿Qué quieres hacer?: ")

        if seleccion == "1":
            print("1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Buscar empleado")
            print("4. Actualizar empleado")
            print("5. Eliminar empleado")
            print("6. Salir")

            while True:
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    registrar_empleado()

                elif opcion == "2":
                    listar_empleados()

                elif opcion == "3":
                    buscar_empleado()

                elif opcion == "4":
                    actualizar_empleado()

                elif opcion == "5":
                    eliminar_empleado()

                elif opcion == "6":
                    break
            
                else:
                    print("Seleccione una opción válida")

        elif opcion == "6":
            print("Hasta luego!")
        else:
            print("Seleccione una opción válida")

if __name__ == "__main__":
    crear_tablas()
    main()

