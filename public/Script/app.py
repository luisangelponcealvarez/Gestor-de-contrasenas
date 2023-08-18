from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import customtkinter
import sqlite3
import random
import string
import pyperclip


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor De Contraseñas")
        self.resizable(False, False)  # Evitar redimensionar la ventana
        self.geometry("750x400")

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, correo TEXT, contrasena TEXT)"
        )
        self.conexion.commit()

    def cargar_datos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, correo, contrasena FROM usuarios")
        rows = cursor.fetchall()
        for row in rows:
            self.tabla.insert("", "end", values=row)

    # ... (el resto de los métodos relacionados con la interfaz gráfica)


if __name__ == "__main__":
    app = App()
    app.mainloop()
