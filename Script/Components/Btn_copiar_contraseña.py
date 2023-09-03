import customtkinter


def btn_copiar_contraseña(self):
    copiar_contrasena_button = customtkinter.CTkButton(
        self, text="Copiar Contraseña", command=self.copiar_contrasena
    )
    copiar_contrasena_button.grid(row=6, column=3, padx=10, pady=10)
