import tkinter as tk
from tkinter import ttk


# Label
class CTkLabel(ttk.Label):
    nombre_label = ttk.Label(ttk.Label, text="Nombre:")
    nombre_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    correo_label = ttk.Label(ttk.Label, text="Correo:")
    correo_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    contrasena_label = ttk.Label(ttk.Label, text="Contraseña:")
    contrasena_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    buscar_label = ttk.Label(ttk.Label, text="Buscar:")
    buscar_label.grid(row=5, column=0, sticky="w", padx=30, pady=5)


# Entry the input
class CTkEntry(ttk.Entry):
    nombre_entry = ttk.Entry(ttk.Entry, textvariable=ttk.Entry.nombre_var)
    nombre_entry.grid(row=1, column=1, columnspan=4, sticky="we", padx=10, pady=5)

    correo_entry = ttk.Entry(ttk.Entry, textvariable=ttk.Entry.correo_var)
    correo_entry.grid(row=2, column=1, columnspan=4, sticky="we", padx=10, pady=5)

    ttk.Entry.contrasena_entry = ttk.Entry(
        ttk.Entry, textvariable=ttk.Entry.contrasena_var, show=""
    )
    ttk.Entry.contrasena_entry.grid(
        row=3, column=1, columnspan=3, sticky="we", padx=10, pady=5
    )

    ttk.Entry.buscar_entry = ttk.Entry(ttk.Entry)
    ttk.Entry.buscar_entry.grid(row=5, column=1, sticky="we", padx=10, pady=5)


#  Button
class CTkButton(ttk.Button):
    generar_button = ttk.Button(
        ttk.Button, text="Generar Contraseña", command=ttk.Button.generar_contrasena
    )
    generar_button.grid(row=3, column=4, padx=10, pady=5)

    # Botón para guardar los datos
    guardar_button = ttk.Button(
        ttk.Button, text="Guardar", command=ttk.Button.guardar_datos
    )
    guardar_button.grid(row=5, column=4, pady=5)

    buscar_button = ttk.Button(
        ttk.Button, text="Buscar", command=ttk.Button.buscar_datos
    )
    buscar_button.grid(row=5, column=2, padx=10, pady=5)

    # Botón para mostrar todos los datos nuevamente
    mostrar_todo_button = ttk.Button(
        ttk.Button, text="Mostrar Todo", command=ttk.Button.mostrar_todo
    )
    mostrar_todo_button.grid(row=5, column=3, padx=10, pady=5)

    # Botón para copiar el nombre
    copiar_nombre_button = ttk.Button(
        ttk.Button, text="Copiar Nombre", command=ttk.Button.copiar_nombre
    )
    copiar_nombre_button.grid(row=6, column=1, padx=10, pady=10)

    # Botón para copiar el correo
    copiar_correo_button = ttk.Button(
        ttk.Button, text="Copiar Correo", command=ttk.Button.copiar_correo
    )
    copiar_correo_button.grid(row=6, column=2, padx=10, pady=5)

    # Botón para copiar la contraseña
    copiar_contrasena_button = ttk.Button(
        ttk.Button, text="Copiar Contraseña", command=ttk.Button.copiar_contrasena
    )
    copiar_contrasena_button.grid(row=6, column=3, padx=10, pady=10)
