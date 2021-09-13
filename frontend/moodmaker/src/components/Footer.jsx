import React from "react";
import { Link as ScrollLink } from "react-scroll";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <div id="subscribe">
      <h3>Moodmaker </h3>
      <div className="footer-social">
        <a href="https://github.com/ysen7-aihub">
          <p>github</p>
        </a>
      </div>

      <p className="footer-p">
        Team 양재역7번출구 | Made using React{" "}
        <span role="img" aria-label="atom">
          ⚛️
        </span>
      </p>
      <br />
    </div>
  );
}

export default Footer;
