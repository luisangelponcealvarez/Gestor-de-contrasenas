import customtkinter


def btn_copiar_correo(self):
    copiar_correo_button = customtkinter.CTkButton(
        self, text="Copiar Correo", command=self.copiar_correo
    )
    copiar_correo_button.grid(row=6, column=2, padx=10, pady=5)
