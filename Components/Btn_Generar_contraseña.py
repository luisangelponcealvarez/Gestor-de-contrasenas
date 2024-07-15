import customtkinter


def Btn_Generar_contraseña(self):
    generar_button = customtkinter.CTkButton(
        self, text="Generar Contraseña", command=self.generar_contrasena
    )
    generar_button.grid(row=3, column=4, padx=10, pady=5)
