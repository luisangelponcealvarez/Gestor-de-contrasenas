from  tkinter import filedialog
import sqlite3


def conexion(self):
    # Selecciónar el archivo
    file = filedialog.askopenfilename()

    # Conectar a la base de datos SQLite
    self.conexion = sqlite3.connect(file)
    self.crear_tabla()
