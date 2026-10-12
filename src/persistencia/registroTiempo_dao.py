from dominio.registroTiempo import RegistroTiempo
from persistencia.conexion import abrir_conexion, marcador_sql

COLUMNAS = "id, id_empleado, id_proyecto, fecha, horasTrabajadas"

def _fila_a_registro(fila):
    return RegistroTiempo(
        id=fila[0],
        id_empleado=fila[1],
        id_proyecto=fila[2],
        fecha=fila[3],
        horas=fila[4],
    )

class RegistroTiempoDAO:

    @staticmethod
    def insertar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "INSERT INTO registroTiempo (id_empleado, id_proyecto, fecha, horasTrabajadas) "
                f"VALUES ({marca}, {marca}, {marca}, {marca})"
            )
            cursor.execute(sql, (registro.id_empleado, registro.id_proyecto, registro.fecha, registro.horas))
            registro.id = cursor.lastrowid
            conexion.commit()
            return registro
        except Exception as e:
            print(f"Error al insertar el registro de tiempo: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE registroTiempo "
                f"SET id_empleado = {marca}, id_proyecto = {marca}, fecha = {marca}, "
                f"horasTrabajadas = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (
                registro.id_empleado,
                registro.id_proyecto,
                registro.fecha,
                registro.horas,
                registro.id,
            ))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el registro de tiempo: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM registroTiempo WHERE id = {marca}"
            cursor.execute(sql, (id_registro,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el registro de tiempo: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM registroTiempo WHERE id = {marca}"
            cursor.execute(sql, (id_registro,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return _fila_a_registro(fila)
        except Exception as e:
            print(f"Error al buscar el registro de tiempo por id: {e}")
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
            cursor.execute(f"SELECT {COLUMNAS} FROM registroTiempo ORDER BY id")
            filas = cursor.fetchall()
            return [_fila_a_registro(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los registros de tiempo: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_por_empleado(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM registroTiempo WHERE id_empleado = {marca} ORDER BY id"
            cursor.execute(sql, (id_empleado,))
            filas = cursor.fetchall()
            return [_fila_a_registro(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los registros de tiempo del empleado: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def listar_por_proyecto(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM registroTiempo WHERE id_proyecto = {marca} ORDER BY id"
            cursor.execute(sql, (id_proyecto,))
            filas = cursor.fetchall()
            return [_fila_a_registro(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los registros de tiempo del proyecto: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()
