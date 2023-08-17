import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Home } from "./Components/Home";
import { Error404 } from "./Components/404";
import { Contacto } from "./Components/Contacto";
import { Creador } from "./Components/Sobre";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Creador" element={<Creador />} />
          <Route path="/Contacto" element={<Contacto />} />
          <Route path="/*" element={<Error404 />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
