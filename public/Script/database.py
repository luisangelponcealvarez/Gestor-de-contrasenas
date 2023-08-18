import sqlite3
import messagebox


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conexion = sqlite3.connect(db_file)
        self.crear_tabla()

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

    def guardar_datos(self, nombre, correo, contrasena):
        nombre = self.nombre_var.get()
        correo = self.correo_var.get()
        contrasena = self.contrasena_var.get()

        if nombre and correo and contrasena:
            # Agregar los datos a la tabla
            self.tabla.insert("", "end", values=(nombre, correo, contrasena))
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Datos guardados correctamente.")

            # Guardar los datos en la base de datos
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)",
                (nombre, correo, contrasena),
            )
            self.conexion.commit()
        else:
            messagebox.showerror("Error", "Por favor, rellene todos los campos.")

    def buscar_datos(self, termino):
        termino = self.buscar_entry.get()
        if termino:
            # Limpiar la tabla antes de mostrar los resultados de búsqueda
            self.tabla.delete(*self.tabla.get_children())

            # Buscar los datos en la base de datos
            cursor = self.conexion.cursor()
            cursor.execute(
                "SELECT nombre, correo, contrasena FROM usuarios WHERE LOWER(nombre) LIKE ? OR LOWER(correo) LIKE ?",
                ("%" + termino.lower() + "%", "%" + termino.lower() + "%"),
            )
            rows = cursor.fetchall()
            for row in rows:
                self.tabla.insert("", "end", values=row)
        else:
            messagebox.showwarning(
                "Advertencia", "Por favor, ingrese un término de búsqueda."
            )

    def cerrar_conexion(self):
        self.conexion.close()
