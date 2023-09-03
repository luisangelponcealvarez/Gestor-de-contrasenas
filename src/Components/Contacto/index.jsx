import "./Contacto.css";
import { useForm, ValidationError } from "@formspree/react";
import Swal from "sweetalert2";
import { Footer } from "../Footer";
import { Header } from "../Header";

export function Contacto() {
  const [state, handleSubmit] = useForm("mbjvgzqa");
  if (state.succeeded) {
    // alert("Gracias por contactarme, te escribiré pronto");
    Swal.fire({
      text: "Gracias por contactarme te contactare muy pronto",
      timer: "8000",
      timerProgressBar: true,
    });
  }

  return (
    <div className="ContainerContact">
      <Header />
      <div className="container">
        <form onSubmit={handleSubmit} className="form">
          <h1>Contacto</h1>
          <p className="text-center">
            Completa el siguiente formulario y me pondré en contacto contigo lo
            antes posible.
            <br />
            Estare feliz en soluciónar sus problemas
          </p>
          <label>Nombre:</label>
          <br />
          <input type="text" name="name" required />
          <br />
          <label>Email:</label>
          <br />
          <input type="email" name="email" required />
          <br />
          <label>Mensaje:</label>
          <br />
          <textarea
            name="message"
            required
            style={{ resize: "none", height: "100px" }}
          />

          <br />
          <ValidationError
            prefix="Message"
            field="message"
            errors={state.errors}
          />
          <button
            type="submit"
            disabled={state.submitting}
            className="btnEnviar cta"
          >
            <span>Enviar email</span>
            <svg viewBox="0 0 13 10" height="10px" width="15px">
              <path d="M1,5 L11,5"></path>
              <polyline points="8 1 12 5 8 9"></polyline>
            </svg>
          </button>
        </form>

        <div className="redes">
          <a
            href="https://www.linkedin.com/in/luis-angel-ponce-alvarez-848826242/"
            target="_blank"
          >
            <i className="fa-brands fa-linkedin Linkedin"></i>
          </a>

          <a
            href="https://www.youtube.com/@LuisAngelPonceAlvarez"
            target="_blank"
          >
            <i className="fa-brands fa-youtube Youtube"></i>
          </a>

          <a href="https://github.com/luisangelponcealvarez/" target="_blank">
            <i className="fa-brands fa-github Github"></i>
          </a>

          <a
            href="https://www.instagram.com/poncealvarezluisangel/"
            target="_blank"
          >
            <i className="fa-brands fa-instagram Instagram"></i>
            {/* <FaInstagram className="Instagram" /> */}
          </a>
          <a
            href="https://www.facebook.com/luisangel.poncealvarez.37"
            target="_blank"
          >
            <i className="fa-brands fa-facebook Facebook"></i>
          </a>

          <a href="https://twitter.com/Luisang01161226" target="_blank">
            <i className="fa-brands fa-twitter Twitter"></i>
          </a>
          <a
            href="https://open.spotify.com/user/nhf5pz5g4wdgjk0bvw2fzhakd?si=1ff6fa2155254f25"
            target="_blank"
          >
            <i className="fa-brands fa-spotify Spotify"></i>
          </a>
        </div>
      </div>
      <Footer />
    </div>
  );
}
