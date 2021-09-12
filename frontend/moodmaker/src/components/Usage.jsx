import React from "react";
import { useEffect } from "react";
import { motion } from "framer-motion";
import { useAnimation } from "framer-motion";
import { useInView } from "react-intersection-observer";
import Card from "./Card";

function Usage() {
  const { ref, inView } = useInView({
    threshold: 0.1
  });
  const animation = useAnimation();

  useEffect(() => {
    if (inView) {
      animation.start({
        y: 0,
        opacity: 1,
        transition: { duration: 0.5, ease: "easeInOut" }
      });
    }
    if (!inView) {
      animation.start({
        y: -100,
        opacity: 0,
        transition: { duration: 0.5, ease: "easeInOut" }
      });
    }
  }, [inView]);

  return (
    <div id="services">
      <div className="s-heading">
        <h1>지금 바로 이용해보세요! 🎵</h1>
        <p></p>
      </div>
      <motion.div ref={ref} animate={animation} className="b-container">
        <Card
          label="View"
          title="01 일기를 업로드한다"
          discipline="AI가 감정을 분석해서 노래를 추천해줄거예요"
          tldr="AI가 감정을 분석해서 당신에게 딱 맞는 노래를 추천해줄거예요"
        />
        <Card
          label="View"
          title="02 풍경 사진을 업로드한다"
          discipline="오늘의 감정에 맞는 풍경 사진을 업로드하세요"
          tldr="오늘의 감정에 맞는 날씨나 풍경 사진을 업로드하세요"
        />
        <Card
          label="View"
          title="03 추천받은 노래를 감상한다"
          discipline="sns 공유 버튼으로 친구들에게 공유해보세요!"
          tldr="sns 공유 버튼으로 주변 사람에게 공유해보세요!"
        />
      </motion.div>
    </div>
  );
}

export default Usage;
