export type State = {
  display: string;
  operator: string | null;
  firstNum: number | null;
  nextNum: boolean;
  memoryNum: number;
};

export enum ActionType {
  All_CLEAR = "AC",
  CLEAR = "C",
  SIGN = "SIGN",
  PERCENTAGE = "PERCENTAGE",
  OPERATOR = "OPERATOR",
  DECIMAL = "DECIMAL",
  NUMBER = "NUMBER",
}

export type Action = {
  type: ActionType | null;
  payload: string;
};
