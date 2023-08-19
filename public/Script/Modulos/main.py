import customtkinter
from tkinter import ttk
from tkinter import filedialog
import sqlite3


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor De Contraseñas")
        self.resizable(False, False)  # Evitar redimensionar la ventana
        self.geometry("750x400")

        # Selecciónar el archivo
        file = filedialog.askopenfilename()

        # Crear variables para almacenar los datos ingresados
        self.nombre_var = customtkinter.StringVar()
        self.correo_var = customtkinter.StringVar()
        self.contrasena_var = customtkinter.StringVar()

        # Conectar a la base de datos SQLite
        self.conexion = sqlite3.connect(file)
        self.crear_tabla()

        # Crear la tabla para mostrar los datos
        self.tabla = ttk.Treeview(
            self, columns=("Nombre", "Correo", "Contraseña"), show="headings"
        )
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Contraseña", text="Contraseña")
        self.tabla.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Crear etiquetas y campos de entrada
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

        # Botón para generar contraseña aleatoria
        generar_button = customtkinter.CTkButton(
            self, text="Generar Contraseña", command=self.generar_contrasena
        )
        generar_button.grid(row=3, column=4, padx=10, pady=5)

        # Botón para guardar los datos
        guardar_button = customtkinter.CTkButton(
            self, text="Guardar", command=self.guardar_datos
        )
        guardar_button.grid(row=5, column=4, pady=5)

        # Crear campo de búsqueda y botón de búsqueda
        buscar_label = customtkinter.CTkLabel(self, text="Buscar:")
        buscar_label.grid(row=5, column=0, sticky="w", padx=30, pady=5)
        self.buscar_entry = customtkinter.CTkEntry(self)
        self.buscar_entry.grid(row=5, column=1, sticky="we", padx=10, pady=5)
        buscar_button = customtkinter.CTkButton(
            self, text="Buscar", command=self.buscar_datos
        )
        buscar_button.grid(row=5, column=2, padx=10, pady=5)

        # Botón para mostrar todos los datos nuevamente
        mostrar_todo_button = customtkinter.CTkButton(
            self, text="Mostrar Todo", command=self.mostrar_todo
        )
        mostrar_todo_button.grid(row=5, column=3, padx=10, pady=5)

        # Botón para copiar el nombre
        copiar_nombre_button = customtkinter.CTkButton(
            self, text="Copiar Nombre", command=self.copiar_nombre
        )
        copiar_nombre_button.grid(row=6, column=1, padx=10, pady=10)

        # Botón para copiar el correo
        copiar_correo_button = customtkinter.CTkButton(
            self, text="Copiar Correo", command=self.copiar_correo
        )
        copiar_correo_button.grid(row=6, column=2, padx=10, pady=5)

        # Botón para copiar la contraseña
        copiar_contrasena_button = customtkinter.CTkButton(
            self, text="Copiar Contraseña", command=self.copiar_contrasena
        )
        copiar_contrasena_button.grid(row=6, column=3, padx=10, pady=10)

        # Cargar los datos desde la base de datos
        self.cargar_datos()

    # Aquí va el componente crear_tabla

    # Aquí va el componente cargar_datos

    # Aquí va el componente guardar_datos

    # Aquí va el componente limpiar_campos

    # Aquí va el componente buscar_datos

    # Aquí va el componente mostrar_todo

    # Aquí va el componente generar_contrasena

    # Aquí va el componente copiar_nombre

    # Aquí va el componente copiar_correo

    # Aquí va el componente copiar_contrasena

    # Aquí va el componente on_closing


if __name__ == "__main__":
    app = App()
    app.mainloop()
