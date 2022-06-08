import React from "react";
import "./Display.css";

type AppProps = {
  value: string;
};

function Display(props: AppProps) {
  return <div className="display">{props.value}</div>;
}

export default Display;
