def limpiar_campos(self):
    self.nombre_var.set("")
    self.correo_var.set("")
    self.contrasena_var.set("")

    # Ocultar la contraseña en el campo de entrada
    self.contrasena_entry.config(show="*")
