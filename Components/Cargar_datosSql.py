def cargar_datos(self):
    cursor = self.conexion.cursor()
    cursor.execute("SELECT nombre, correo, contrasena FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        self.tabla.insert("", "end", values=row)
