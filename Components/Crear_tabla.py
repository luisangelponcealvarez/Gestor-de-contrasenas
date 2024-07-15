from tkinter import ttk

# Crear la tabla para mostrar los datos


def Crear_tabla(self):
    self.tabla = ttk.Treeview(
        self, columns=("Nombre", "Correo", "Contraseña"), show="headings"
    )
    self.tabla.heading("Nombre", text="Nombre")
    self.tabla.heading("Correo", text="Correo")
    self.tabla.heading("Contraseña", text="Contraseña")
    self.tabla.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
