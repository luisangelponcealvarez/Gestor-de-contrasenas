def crear_tabla(self):
    cursor = self.conexion.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, correo TEXT, contrasena TEXT)"
    )
    self.conexion.commit()
