import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./styles.css";

import Home from "./components/Home";
import Navbar from "./components/Navbar";
import ScrollToTop from "./components/ScrollToTop";
import Footer from "./components/Footer";
import Usage from "./components/Usage";
import UploadPhoto from "./components/UploadPhoto";
import UploadText from "./components/UploadText";
import Resultpage from "./components/Resultpage";

export default function App() {
  return (
    <Router>
      <ScrollToTop />
      <Switch>
        <>
          <div className="App">
            <Navbar />
            <Route path="/" exact component={Home} />
            <Route path="/usage" component={Usage} />
            <Route path="/uploadphoto" component={UploadPhoto} />
            <Route path="/uploadtext" component={UploadText} />
            <Route path="/result" component={Resultpage} />

            <Footer />
          </div>
        </>
      </Switch>
    </Router>
  );
}
