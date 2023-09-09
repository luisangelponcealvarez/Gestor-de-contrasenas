import { Link } from "react-router-dom";
import "./Header.css";
import React, { useState } from "react";
import logo from "../../../public/Img/logo.png";

export function Header() {
  // // manipulación del menu del celular
  const [menu, mostrar] = useState(false);

  const toggleMenu = () => {
    mostrar(!menu);
  };

  return (
    <div className="contenedor">
      <header id="container-nav">
        <a href="/">
          <img src={logo} alt="logo" className="logo-img" />
        </a>

        <label className="burger">
          <input type="checkbox" id="burger" onClick={toggleMenu} />
          <span></span>
          <span></span>
          <span></span>
        </label>

        <nav id="menu" className={`menu ${menu ? "mostrar" : ""}`}>
          <ul>
            <li>
              <Link to="/">Inicio</Link>
            </li>
            <li>
              <Link to="/Creador">Creador</Link>
            </li>
            <li>
              <a href="https://luisangelponcealvarez.netlify.app/Contact">
                Contacto
              </a>
            </li>
          </ul>
        </nav>
      </header>
    </div>
  );
}
