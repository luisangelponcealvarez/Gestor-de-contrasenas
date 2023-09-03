import { Link } from "react-router-dom";
import image from "../../../public/Img/404.png";
import "./404.css";

export function Error404() {
  return (
    <div className="Error404">
      <div className="img_404">
        <img className="image-404 m-3" src={image} alt="404" />
      </div>
      <p className="notfound-text">
        Esta página no existe o esta en mantenimiento
      </p>
      {/* <p className="notfound-text">Esta página esta en proceso de creación</p> */}
      <Link to="/" className="btnHome btn btn-secondary m-3">
        Home
      </Link>
    </div>
  );
}
