from dominio.proyecto import Proyecto
from persistencia.conexion import abrir_conexion, marcador_sql

COLUMNAS = "id, nombre, descripcion, fechaInicio"

def _fila_a_proyecto(fila):
    return Proyecto(
        id=fila[0],
        nombre=fila[1],
        descripcion=fila[2],
        fechaInicio=fila[3],
    )

class ProyectoDAO:

    @staticmethod
    def insertar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO proyecto (nombre, descripcion, fechaInicio) VALUES ({marca}, {marca}, {marca})"
            cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fechaInicio))
            proyecto.id = cursor.lastrowid
            conexion.commit()
            return proyecto
        except Exception as e:
            print(f"Error al insertar el proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return None
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE proyecto "
                f"SET nombre = {marca}, descripcion = {marca}, fechaInicio = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fechaInicio, proyecto.id))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar el proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def eliminar(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT {COLUMNAS} FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return _fila_a_proyecto(fila)
        except Exception as e:
            print(f"Error al buscar el proyecto por id: {e}")
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
            cursor.execute(f"SELECT {COLUMNAS} FROM proyecto ORDER BY id")
            filas = cursor.fetchall()
            return [_fila_a_proyecto(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los proyectos: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()


    @staticmethod
    def asignar_empleado(id_proyecto, id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES ({marca}, {marca})"
            cursor.execute(sql, (id_empleado, id_proyecto))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al asignar el empleado al proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
        finally:
            if conexion is not None:
                conexion.close()

    @staticmethod
    def quitar_empleado(id_proyecto, id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM empleado_proyecto WHERE id_empleado = {marca} AND id_proyecto = {marca}"
            cursor.execute(sql, (id_empleado, id_proyecto))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al quitar el empleado del proyecto: {e}")
            if conexion is not None:
                conexion.rollback()
            return False
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
            columnas = ", ".join(f"p.{c.strip()}" for c in COLUMNAS.split(","))
            sql = (
                f"SELECT {columnas} FROM proyecto p "
                "JOIN empleado_proyecto ep ON ep.id_proyecto = p.id "
                f"WHERE ep.id_empleado = {marca} ORDER BY p.id"
            )
            cursor.execute(sql, (id_empleado,))
            filas = cursor.fetchall()
            return [_fila_a_proyecto(f) for f in filas]
        except Exception as e:
            print(f"Error al listar los proyectos del empleado: {e}")
            return []
        finally:
            if conexion is not None:
                conexion.close()
