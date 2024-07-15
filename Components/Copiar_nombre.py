import messagebox, pyperclip


def copiar_nombre(self):
    seleccion = self.tabla.focus()
    if seleccion:
        nombre = self.tabla.item(seleccion)["values"][0]
        pyperclip.copy(nombre)
        messagebox.showinfo("Éxito", "Nombre copiado al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un registro.")
