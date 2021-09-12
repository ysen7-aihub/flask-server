import React from "react";
import { motion } from "framer-motion";

function Card(props) {
  return (
    <motion.section
      whileHover={{
        scale: 1.05,
        transition: { duration: 0.3 }
      }}
      id="project"
    >
      <div className="wrapper">
        <div className="projectlayout">
          <img src={props.image} alt={props.alt} />
          <div className="projecttext">
            <h2>{props.title}</h2>
            <p>{props.tldr}</p>
          </div>
        </div>
      </div>
    </motion.section>
  );
}

export default Card;
