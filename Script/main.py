import customtkinter

# Import Modulos

from Components import (
    Copiar_nombre,
    Copiar_correo,
    Copiar_Contraseña,
    Crear_tabla,
    AlmacenarDatos,
    Conexion,
    Campos,
    Btn_Generar_contraseña,
    Btn_Guardar,
    InputBuscar,
    Btn_mostrar_todo,
    Btn_copiar_nombre,
    Btn_copiar_correo,
    Btn_copiar_contraseña,
    Cargar_datos,
    SqlTabla,
    Cargar_datosSql,
    Guardar_datos,
    Limpiar_campos,
    Buscar_datos,
    Mostrar,
    Generar_contraseña,
)


class GestorDeContraseñas(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor De Contraseñas")
        self.resizable(False, False)  # Evitar redimensionar la ventana
        self.geometry("750x400")

        # Crear variables para almacenar los datos ingresados
        AlmacenarDatos.AlmacenarDatos(self)

        # Conectar a la base de datos SQLite
        Conexion.conexion(self)

        # Crear la tabla para mostrar los datos
        Crear_tabla.Crear_tabla(self)

        # Crear etiquetas y campos de entrada
        Campos.campos(self)

        # Botón para generar contraseña aleatoria
        Btn_Generar_contraseña.Btn_Generar_contraseña(self)

        # Botón para guardar los datos
        Btn_Guardar.Btn_buardar(self)

        # Crear campo de búsqueda y botón de búsqueda
        InputBuscar.InputBuscar(self)

        # Botón para mostrar todos los datos nuevamente
        Btn_mostrar_todo.Btn_mostrar_todo(self)

        # Botón para copiar el nombre
        Btn_copiar_nombre.Btn_copiar_nombre(self)

        # Botón para copiar el correo
        Btn_copiar_correo.btn_copiar_correo(self)

        # Botón para copiar la contraseña
        Btn_copiar_contraseña.btn_copiar_contraseña(self)

        # Cargar los datos desde la base de datos
        Cargar_datos.cargar_datos(self)

    def crear_tabla(self):
        SqlTabla.Sql(self)

    def cargar_datos(self):
        Cargar_datosSql.cargar_datos(self)

    def guardar_datos(self):
        Guardar_datos.guardar_datos(self)

    def limpiar_campos(self):
        Limpiar_campos.limpiar_campos(self)

    def buscar_datos(self):
        Buscar_datos.buscar(self)

    def mostrar_todo(self):
        Mostrar.Mostrar(self)

    def generar_contrasena(self):
        Generar_contraseña.generar_contraseña(self)

    def copiar_nombre(self):
        Copiar_nombre.copiar_nombre(self)

    def copiar_correo(self):
        Copiar_correo.copiar_correo(self)

    def copiar_contrasena(self):
        Copiar_Contraseña.copiar_contraseña(self)

    def on_closing(self):
        self.conexion.close()
        self.destroy()


if __name__ == "__main__":
    app = GestorDeContraseñas()
    app.mainloop()
