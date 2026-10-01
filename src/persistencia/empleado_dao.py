from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO empleado (nombre, direccion, numeracion, telefono, correo, salario, inicioContrato)
            VALUES ({marcador}, {marcador}, {marcador}, {marcador}, {marcador}, {marcador}, {marcador})
        """

        cursor.execute(sql, (empleado.nombre, empleado.direccion, empleado.numeracion, empleado.telefono, empleado.correo, empleado.salario, empleado.inicioContrato))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
    
        marca = marcador_sql()
        sql = f"""
                SELECT id, nombre, correo
                FROM empleado WHERE id = {marca}
            """
    
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
    
        if fila is None:
            return None
    
        return Empleado(id=fila[0], nombre=fila[1], correo=fila[2])

    
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
    
   
