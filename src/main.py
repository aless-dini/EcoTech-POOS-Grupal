from persistencia.crear_bd import crear_tablas
from menus.menuPrincipal import menu_principal

def main():
    crear_tablas()
    print("Base de datos preparada correctamente.")
    menu_principal()

if __name__ == "__main__":
    main()
