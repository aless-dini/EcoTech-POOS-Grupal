from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO empleado (nombre, correo)
            VALUES ({marcador}, {marcador})
        """

        cursor.execute(sql, (empleado.nombre, empleado.correo))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    
    @staticmethod
    def actualizar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "UPDATE empleado "
            f"SET nombre = {marca}, correo = {marca} "
            f"WHERE id = {marca}"
        )
            
        cursor.execute(
            sql,
            (
                empleado.nombre,
                empleado.correo,
                empleado.id
            )  
        )

        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()

        return filas_afectadas > 0


    @staticmethod
    def eliminar(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "DELETE FROM empleado "
            f"WHERE id = {marca}"
        )

        cursor.execute(sql, (id_empleado,))
        conexion.commit()

        eliminado = cursor.rowcount > 0

        conexion.close()
        return eliminado
    
   
