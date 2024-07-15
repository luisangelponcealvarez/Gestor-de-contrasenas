import pyperclip, messagebox


def copiar_contraseña(self):
    seleccion = self.tabla.focus()
    if seleccion:
        contrasena = self.tabla.item(seleccion)["values"][2]
        pyperclip.copy(contrasena)
        messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un registro.")
