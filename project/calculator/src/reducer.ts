import { State, Action, ActionType } from "./types";

export const INITIAL_STATE: State = {
  display: "0",
  firstNum: null,
  nextNum: false,
  operator: null,
  memoryNum: 0,
};

export default function reducer(state: State, action: Action): State {
  const { type, payload } = action;
  switch (type) {
    case ActionType.All_CLEAR: {
      return {
        ...state,
        display: "0",
        firstNum: null,
        nextNum: false,
        operator: null,
      };
    }

    case ActionType.CLEAR: {
      return {
        ...state,
        display: "0",
      };
    }

    case ActionType.NUMBER: {
      const number = payload;
      let { display, nextNum } = state;

      if (state.nextNum) {
        display = number;
        nextNum = false;
      } else {
        display = display === "0" ? number : display + number;
      }
      return {
        ...state,
        display,
        nextNum,
      };
    }

    case ActionType.DECIMAL: {
      let { display, nextNum } = state;
      if (nextNum) return state;

      if (!display.includes(".")) {
        display += ".";
      }
      return { ...state, display };
    }

    case ActionType.OPERATOR: {
      const nextOperator = payload;
      let { firstNum, display, operator } = state;
      const inputValue = parseFloat(display);

      if (operator && state.nextNum) {
        return { ...state, operator: nextOperator };
      }

      if (firstNum === null) {
        firstNum = inputValue;
      } else if (operator) {
        display = performCalculation[operator](firstNum, inputValue).toString();
        firstNum = parseFloat(display);
      }

      return {
        ...state,
        display,
        firstNum,
        nextNum: true,
        operator: nextOperator,
      };
    }

    case ActionType.PERCENTAGE: {
      let { display } = state;
      display = (parseFloat(display) / 100).toString();
      return { ...state, display };
    }

    case ActionType.SIGN: {
      let { display, firstNum, nextNum } = state;
      display = (parseFloat(display) * -1).toString();
      if (nextNum) {
        firstNum = parseFloat(display);
      }
      return { ...state, display, firstNum };
    }

    default:
      return state;
  }
}

type Operations = {
  [operator: string]: (firstNum: number, secondNum: number) => number;
};

const performCalculation: Operations = {
  "/": (firstNum, secondNum) => firstNum / secondNum,

  "*": (firstNum, secondNum) => firstNum * secondNum,

  "+": (firstNum, secondNum) => firstNum + secondNum,

  "-": (firstNum, secondNum) => firstNum - secondNum,

  "=": (firstNum, secondNum) => secondNum,
};
