import customtkinter


def Btn_buardar(self):
    guardar_button = customtkinter.CTkButton(
        self, text="Guardar", command=self.guardar_datos
    )
    guardar_button.grid(row=5, column=4, pady=5)
