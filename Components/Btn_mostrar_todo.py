import customtkinter


def Btn_mostrar_todo(self):
    mostrar_todo_button = customtkinter.CTkButton(
        self, text="Mostrar Todo", command=self.mostrar_todo
    )
    mostrar_todo_button.grid(row=5, column=3, padx=10, pady=5)
