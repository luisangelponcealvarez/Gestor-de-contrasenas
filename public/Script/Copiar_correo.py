import pyperclip
import messagebox


def copiar_correo(self):
    seleccion = self.tabla.focus()
    if seleccion:
        correo = self.tabla.item(seleccion)["values"][1]
        pyperclip.copy(correo)
        messagebox.showinfo("Éxito", "Correo copiado al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un registro.")
