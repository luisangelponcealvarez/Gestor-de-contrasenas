import messagebox


def buscar(self):
    termino = self.buscar_entry.get()
    if termino:
        # Limpiar la tabla antes de mostrar los resultados de búsqueda
        self.tabla.delete(*self.tabla.get_children())

        # Buscar los datos en la base de datos
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT nombre, correo, contrasena FROM usuarios WHERE LOWER(nombre) LIKE ? OR LOWER(correo) LIKE ?",
            ("%" + termino.lower() + "%", "%" + termino.lower() + "%"),
        )
        rows = cursor.fetchall()
        for row in rows:
            self.tabla.insert("", "end", values=row)
    else:
        messagebox.showwarning(
            "Advertencia", "Por favor, ingrese un término de búsqueda."
        )
