const currentDisplay = document.querySelector(".current-display");
const previousDisplay = document.querySelector(".previous-display");

let firstOperand = "";
let secondOperand = "";
let result;
let operator;

const calculatorNumberButtons = document.querySelectorAll("[data-number]");
calculatorNumberButtons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.textContent === "." && currentDisplay.textContent.includes("."))
      return;

    if (result) {
      firstOperand = button.textContent;
      result = "";
    } else {
      firstOperand += button.textContent;
    }
    currentDisplay.textContent = firstOperand;
  });
});

const calculatorOperatorButtons = document.querySelectorAll("[data-operation]");
calculatorOperatorButtons.forEach((button) => {
  button.addEventListener("click", () => {
    if (currentDisplay.textContent === "") return;

    if (firstOperand && secondOperand) calculate();

    operator = button.textContent;
    secondOperand = firstOperand;
    previousDisplay.textContent = secondOperand + operator;
    currentDisplay.textContent = "";
    firstOperand = "";
  });
});

const clearDisplay = document.querySelector("[data-all-clear]");
clearDisplay.addEventListener("click", clear);
function clear() {
  currentDisplay.textContent = "";
  previousDisplay.textContent = "";
  firstOperand = "";
  secondOperand = "";
  operator = "";
}

const deleteLastCharacter = document.querySelector("[data-delete]");
deleteLastCharacter.addEventListener("click", removeCharacter);

function removeCharacter() {
  let displayString = currentDisplay.textContent;
  let deleteLastCharacter = displayString.slice(0, -1);
  currentDisplay.textContent = deleteLastCharacter;
  firstOperand = deleteLastCharacter;
}

const equalButton = document.querySelector("[data-equals]");
equalButton.addEventListener("click", calculate);

function calculate() {
  if (currentDisplay.textContent === "") return;

  if (secondOperand.length > 0 || firstOperand.length > 0) {
    secondOperand = parseFloat(secondOperand);
    firstOperand = parseFloat(firstOperand);
  }

  switch (operator) {
    case "+":
      result = secondOperand + firstOperand;
      break;
    case "-":
      result = secondOperand - firstOperand;
      break;
    case "÷":
      result = secondOperand / firstOperand;
      break;
    case "*":
      result = secondOperand * firstOperand;
      break;
    default:
      return;
  }
  firstOperand = result;
  secondOperand = "";
  currentDisplay.textContent = result;
}
