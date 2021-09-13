import React, { useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Link } from "react-router-dom";
import MyResponsiveRadar from "./Chart";
import Music from "./Music";
import API from "../utils/api";
import Label from "./Label";

function ResultPage() {
  const content = [];
  const data = [];
  const ex = [
    {
      artist: "Bessie Smith",
      name: "Me and My Gin",
      src: "https://www.youtube.com/embed/Bs35gRQP0MM"
    },
    {
      artist: "Louis Armstrong",
      name: "Lazy River",
      src: "https://www.youtube.com/embed/cJBAmeowNeU"
    },
    {
      artist: "Fletcher Henderson & His Orche",
      name: "Naughty Man",
      src: "https://www.youtube.com/embed/7NWexL-wI1c"
    }
  ];

  useEffect(() => {
    API
      .get("http://172.30.1.8:80/predict/")
      .then(response => {
        console.log(response.data);
        rendering(response.data);
      })
      .catch(response => {
        console.log(response);
      });
  }, []);

  const rendering = res => {
    for (let i = 0; i < res.length; i++) {
      if (i < 3) {
        content.push(res[i]);
      } else {
        data.push(res[i]);
      }
    }
    console.log(data);
  };

  return (
    <AnimatePresence>
      <motion.div
        exit={{ opacity: 0 }}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
      >
        <div className="r-main">
          <div className="photo">
            <div className="c-container">
              <h2>🎉 음악 추천 결과가 도착했어요!</h2>
              <div className="chart">
                <MyResponsiveRadar data={data} />
              </div>
            </div>
            <Music content={ex} />
            <Label />

            {/*<Layout />*/}
          </div>
        </div>
      </motion.div>
    </AnimatePresence>
  );
}

export default ResultPage;
