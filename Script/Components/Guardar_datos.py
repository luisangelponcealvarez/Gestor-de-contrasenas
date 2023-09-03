import messagebox


def guardar_datos(self):
    nombre = self.nombre_var.get()
    correo = self.correo_var.get()
    contrasena = self.contrasena_var.get()
    if nombre and correo and contrasena:
        # Agregar los datos a la tabla
        self.tabla.insert("", "end", values=(nombre, correo, contrasena))
        self.limpiar_campos()
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")

        # Guardar los datos en la base de datos
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)",
            (nombre, correo, contrasena),
        )
        self.conexion.commit()
    else:
        messagebox.showerror("Error", "Por favor, rellene todos los campos.")
