import { Footer } from "../Footer";
import { Header } from "../Header";
import "./Sobre.css";

export function Creador() {
  return (
    <>
      <Header />
      <section id="Creador">
        <img
          src="https://avatars.githubusercontent.com/u/103376624?v=4"
          className="photo"
          alt="photo"
        />

        <div className="container-text m-2">
          <h1>Luis Angel Ponce Alvarez</h1>
          <p className="descripción">
            Estudiante de programación enfocado al Desarrollo Web Frontend. Como
            persona amante a los diseños intuitivos y estéticamente agradables
            busco crear proyectos que brinden la mejor experiencia para el
            usuario.
          </p>
          <a href="https://luisangelponcealvarez.netlify.app/Luis_Angel_Ponce_Alvarez_Cv.pdf">
            <button className="button m-2">
              <span className="button-content">Download Cv</span>
            </button>
          </a>
        </div>
      </section>
      <Footer />
    </>
  );
}
