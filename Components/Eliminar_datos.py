import messagebox


def editar_datos(self):
    seleccion = self.tabla.focus()
    if seleccion:
        datos_seleccionados = self.tabla.item(seleccion)["values"]
        if datos_seleccionados:
            # Cargar datos seleccionados en los campos de entrada para su edición
            self.nombre_var.set(datos_seleccionados[0])
            self.correo_var.set(datos_seleccionados[1])
            self.contrasena_var.set(datos_seleccionados[2])


def eliminar_datos(self):
    seleccion = self.tabla.focus()
    if seleccion:
        confirmacion = messagebox.askyesno(
            "Confirmar Eliminación", "¿Seguro que desea eliminar este registro?"
        )
        if confirmacion:
            # Eliminar el registro seleccionado de la tabla
            self.tabla.delete(seleccion)

            # Eliminar el registro seleccionado de la base de datos
            cursor = self.conexion.cursor()
            cursor.execute(
                "DELETE FROM usuarios WHERE nombre = ? AND correo = ? AND contrasena = ?",
                self.tabla.item(seleccion)["values"],
            )
            self.conexion.commit()
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un registro.")
