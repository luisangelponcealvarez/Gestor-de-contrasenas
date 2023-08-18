import string
import random


def generar_contrasena(self):
    longitud = 20
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    self.contrasena_var.set(contrasena)
