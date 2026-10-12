from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion, marcador_sql

COLUMNAS = "id, id_empleado, nombre, contraseña, rol"

def _fila_a_usuario(fila):
    return Usuario.desde_bd(
        id=fila[0],
        id_empleado=fila[1],
        nombre=fila[2],
        contraseña_cifrada=fila[3],
        rol=fila[4],
    )

class UsuarioDAO:

    @staticmethod
    def insertar(usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "INSERT INTO usuario (id_empleado, nombre, contraseña, rol) "
                f"VALUES ({marca}, {marca}, {marca}, {marca})"
            )
            cursor.execute(sql, (usuario.id_empleado, usuario.nombre, usuario.contraseña, usuario.rol))
            usuario.id = cursor.lastrowid
            conexion.commit()
            return usuario
        except Exception as e:
            print(f"Error al insertar el usuario: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE usuario "
                f"SET id_empleado = {marca}, nombre = {marca}, contraseña = {marca}, rol = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (usuario.id_empleado, usuario.nombre, usuario.contraseña, usuario.rol, usuario.id))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el usuario: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_usuario):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM usuario WHERE id = {marca}"
            cursor.execute(sql, (id_usuario,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_nombre(nombre):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM usuario WHERE nombre = {marca}"
            cursor.execute(sql, (nombre,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return _fila_a_usuario(fila)
        except Exception as e:
            print(f"Error al buscar el usuario: {e}")
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_todos():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute(f"SELECT {COLUMNAS} FROM usuario ORDER BY id")
            filas = cursor.fetchall()
            return [_fila_a_usuario(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los usuarios: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()
