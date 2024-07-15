import customtkinter


def InputBuscar(self):
    buscar_label = customtkinter.CTkLabel(self, text="Buscar:")
    buscar_label.grid(row=5, column=0, sticky="w", padx=30, pady=5)
    self.buscar_entry = customtkinter.CTkEntry(self)
    self.buscar_entry.grid(row=5, column=1, sticky="we", padx=10, pady=5)
    buscar_button = customtkinter.CTkButton(
        self, text="Buscar", command=self.buscar_datos
    )
    buscar_button.grid(row=5, column=2, padx=10, pady=5)
