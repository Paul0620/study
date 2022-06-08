import React, { useState, Dispatch, SetStateAction } from "react";
import Buttons from "./Buttons";
import Display from "./Display";
import "./App.css";

type propTypes = {
  total: null;
};

function App() {
  return (
    <div className="App">
      <Display />
      <Buttons />
    </div>
  );
}

export default App;
