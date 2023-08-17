import "./Inicio.css";

export function Inicio() {
  return (
    <>
      <section id="inicio">
        <img
          src="https://github.com/luisangelponcealvarez/Gestor-de-contrasenas/raw/main/miniatura.png"
          className="miniatura"
          alt="photo"
        />

        <div className="container-text">
          <h1>Gestor De Contraseñas</h1>
          <p className="descripción">
            El Gestor de Contraseñas en Python con CustomTkinter y SQL es una
            aplicación que brinda seguridad y comodidad en la gestión de
            contraseñas. Utiliza una interfaz intuitiva creada con CustomTkinter
            y almacena las contraseñas de manera segura en una base de datos
            SQL. Las contraseñas se cifran antes de almacenarse y solo pueden
            accederse con una contraseña maestra. Ofrece funciones para agregar,
            ver y editar contraseñas, incluyendo un generador de contraseñas
            seguras y una copia segura al portapapeles. En resumen, es una
            solución práctica y segura para gestionar contraseñas de forma
            eficiente.
          </p>
          <a href="https://github.com/luisangelponcealvarez/Gestor-de-contrasenas/archive/refs/tags/v1.zip">
            <button className="button m-2">
              <span className="button-content">Download</span>
            </button>
          </a>
        </div>
      </section>
    </>
  );
}
