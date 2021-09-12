import React from "react";
import { motion } from "framer-motion";
import WaveLine from "./WaveLine";
import { Link } from "react-router-dom";

function Header(props) {
  return (
    <motion.div
      animate={{
        opacity: 1
      }}
      transition={{ ease: "easeInOut", duration: 0.3 }}
      initial={{ opacity: 0 }}
      id="topofpage"
      className="main"
    >
      <WaveLine />

      <div className="name">
        <motion.h1
          id="hello"
          animate={{
            opacity: 1,
            y: 0
          }}
          transition={{ ease: "easeInOut", delay: 0.5, duration: 0.5 }}
          initial={{ opacity: 0, y: 50 }}
        >
          <span>Moodmaker</span>
          <span id="wave-emoji" role="img" aria-label="wave">
            🎶
          </span>
        </motion.h1>

        <motion.p
          className="details"
          animate={{
            opacity: 1,
            y: 0
          }}
          transition={{ ease: "easeInOut", delay: 1, duration: 0.5 }}
          initial={{ opacity: 0, y: 50 }}
        >
          일기와 이미지를 넣으면 감정을 분석해서 <br />
          음악을 추천해주는 AI 웹서비스입니다
        </motion.p>
        <motion.div
          className="header-btns"
          animate={{
            opacity: 1
          }}
          transition={{ ease: "easeInOut", delay: 1.5, duration: 0.5 }}
          initial={{ opacity: 0 }}
        >
          <Link to={props.path} className="logo">
            <button className="cv-btn">시작하기</button>
          </Link>
        </motion.div>
      </div>
    </motion.div>
  );
}

export default Header;
