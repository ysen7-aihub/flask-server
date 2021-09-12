import React from "react";
import { Link as ScrollLink } from "react-scroll";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <>
      <div>
        <nav>
          <Link to="/" className="logo">
            Moodmaker
          </Link>

          <ul className="menu">
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <ScrollLink to="services" smooth={true}>
                Usage
              </ScrollLink>
            </li>
            <li>
              <ScrollLink to="features" smooth={true}>
                Start
              </ScrollLink>
            </li>
          </ul>
        </nav>
      </div>
    </>
  );
}

export default Navbar;
