import customtkinter


def Btn_copiar_nombre(self):
    copiar_nombre_button = customtkinter.CTkButton(
        self, text="Copiar Nombre", command=self.copiar_nombre
    )
    copiar_nombre_button.grid(row=6, column=1, padx=10, pady=10)
