import customtkinter
import messagebox


def editar_datos(self):
    seleccion = self.tabla.focus()
    if seleccion:
        # Obtener los datos actuales
        nombre_actual = self.tabla.item(seleccion)["values"][0]
        correo_actual = self.tabla.item(seleccion)["values"][1]
        contrasena_actual = self.tabla.item(seleccion)["values"][2]

        # Mostrar una ventana de edición con los datos actuales
        ventana_edicion = customtkinter.CTk()
        ventana_edicion.title("Editar Datos")
        ventana_edicion.geometry("400x200")

        nombre_label = customtkinter.CTkLabel(ventana_edicion, text="Nuevo Nombre:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)
        nuevo_nombre_var = customtkinter.StringVar(value=nombre_actual)
        nombre_entry = customtkinter.CTkEntry(
            ventana_edicion, textvariable=nuevo_nombre_var
        )
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        correo_label = customtkinter.CTkLabel(ventana_edicion, text="Nuevo Correo:")
        correo_label.grid(row=1, column=0, padx=10, pady=10)
        nuevo_correo_var = customtkinter.StringVar(value=correo_actual)
        correo_entry = customtkinter.CTkEntry(
            ventana_edicion, textvariable=nuevo_correo_var
        )
        correo_entry.grid(row=1, column=1, padx=10, pady=10)

        contrasena_label = customtkinter.CTkLabel(
            ventana_edicion, text="Nueva Contraseña:"
        )
        contrasena_label.grid(row=2, column=0, padx=10, pady=10)
        nuevo_contrasena_var = customtkinter.StringVar(value=contrasena_actual)
        contrasena_entry = customtkinter.CTkEntry(
            ventana_edicion, textvariable=nuevo_contrasena_var, show=""
        )
        contrasena_entry.grid(row=2, column=1, padx=10, pady=10)

        # Función para actualizar los datos en la tabla y la base de datos
        def actualizar_datos():
            nuevo_nombre = nuevo_nombre_var.get()
            nuevo_correo = nuevo_correo_var.get()
            nueva_contrasena = nuevo_contrasena_var.get()

            # Actualizar en la tabla
            self.tabla.item(
                seleccion, values=(nuevo_nombre, nuevo_correo, nueva_contrasena)
            )

            # Actualizar en la base de datos
            cursor = self.conexion.cursor()
            cursor.execute(
                "UPDATE usuarios SET nombre=?, correo=?, contrasena=? WHERE nombre=? AND correo=? AND contrasena=?",
                (
                    nuevo_nombre,
                    nuevo_correo,
                    nueva_contrasena,
                    nombre_actual,
                    correo_actual,
                    contrasena_actual,
                ),
            )
            self.conexion.commit()

            ventana_edicion.destroy()

        # Botón para guardar los cambios
        guardar_cambios_button = customtkinter.CTkButton(
            ventana_edicion, text="Guardar Cambios", command=actualizar_datos
        )
        guardar_cambios_button.grid(row=3, column=0, columnspan=2, pady=10)

        ventana_edicion.mainloop()
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un registro.")
