import React from "react";
import { motion, AnimatePresence } from "framer-motion";

import Header from "./Header";
import Usage from "./Usage";
import UploadPhoto from "./UploadPhoto";
import UploadText from "./UploadText";

function Home() {
  return (
    <AnimatePresence>
      <motion.div
        exit={{ opacity: 0 }}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
      >
        <Header path="/UploadText" />
        <Usage />
        <UploadText />
      </motion.div>
    </AnimatePresence>
  );
}

export default Home;
