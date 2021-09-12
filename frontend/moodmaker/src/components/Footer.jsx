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
      <div className="footer">
        <Link to="/" smooth={true.toString()}>
          <p>Home</p>
        </Link>

        <ScrollLink to="services" smooth={true}>
          <p>Projects</p>
        </ScrollLink>

        <ScrollLink to="features" smooth={true}>
          <p>Upload</p>
        </ScrollLink>
      </div>
      <p className="footer-p">
        Team 양재역7번출구 | Made using React{" "}
        <span role="img" aria-label="atom">
          ⚛️
        </span>
      </p>
      <br />
      <ScrollLink to="topofpage" smooth={true} className="to-top-btn">
        <p>위로 올라가기</p>
      </ScrollLink>
    </div>
  );
}

export default Footer;
