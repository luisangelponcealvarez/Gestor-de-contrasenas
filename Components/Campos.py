import customtkinter


def campos(self):
    nombre_label = customtkinter.CTkLabel(self, text="Nombre:")
    nombre_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    nombre_entry = customtkinter.CTkEntry(self, textvariable=self.nombre_var)
    nombre_entry.grid(row=1, column=1, columnspan=4, sticky="we", padx=10, pady=5)

    correo_label = customtkinter.CTkLabel(self, text="Correo:")
    correo_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    correo_entry = customtkinter.CTkEntry(self, textvariable=self.correo_var)
    correo_entry.grid(row=2, column=1, columnspan=4, sticky="we", padx=10, pady=5)

    contrasena_label = customtkinter.CTkLabel(self, text="Contraseña:")
    contrasena_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    self.contrasena_entry = customtkinter.CTkEntry(
        self, textvariable=self.contrasena_var, show=""
    )
    self.contrasena_entry.grid(
        row=3, column=1, columnspan=3, sticky="we", padx=10, pady=5
    )
