def on_closing(self):
    self.conexion.close()
    self.destroy()
