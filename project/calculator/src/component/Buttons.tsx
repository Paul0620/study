import React from "react";
import { ActionType } from "../types";
import { Context } from "./Context";
import "./Buttons.css";

type btnProps = {
  children: React.ReactNode;
  type: keyof typeof ActionType;
  value: string;
};

const Button = ({ type, value, children }: btnProps) => {
  const [, dispatch] = React.useContext(Context);
  const actionPayload = (value && value.toString()) || children?.toString();

  const handleClick = () => {
    dispatch && dispatch({ type: ActionType[type], payload: actionPayload });
  };

  return <>{children}</>;
};

function Buttons() {
  return (
    <div className="buttonPanel">
      <div className="col1">
        <Button type="AC">AC</Button>
        {/* <Button name="+/-" />
        <Button name="%" />
        <Button name="÷" />
      </div>
      <div className="col2">
        <Button name="7" />
        <Button name="8" />
        <Button name="9" />
        <Button name="x" />
      </div>
      <div className="col3">
        <Button name="4" />
        <Button name="5" />
        <Button name="6" />
        <Button name="-" />
      </div>
      <div className="col4">
        <Button name="1" />
        <Button name="2" />
        <Button name="3" />
        <Button name="+" />
      </div>
      <div className="col5">
        <Button name="0" />
        <Button name="." />
        <Button name="=" /> */}
      </div>
    </div>
  );
}
export default Buttons;
