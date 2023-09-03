def Mostrar(self):
    # Limpiar la tabla antes de mostrar todos los datos
    self.tabla.delete(*self.tabla.get_children())

    # Cargar los datos desde la base de datos
    self.cargar_datos()
