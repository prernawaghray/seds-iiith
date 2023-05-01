let isOperator;
let isDot;
let isNumber;

let btns = document.querySelectorAll(".num-button");
let resultBox = document.querySelector("#result-box");
let clearBtn = document.querySelector('#clear');
let backBtn = document.querySelector('#back');

let total = document.querySelector("#total");

let btnSpread = [...btns];

//Function to clear all the digits on screen
function clearCalculator() {
    isOperator = true;
    isDot = false;
    isNumber = true;
    resultBox.innerHTML = "0"
}
clearCalculator();

// Function to backspace a digit
function backSpace() {
    if(isNumber == true)
        resultBox.innerHTML = resultBox.innerHTML.slice(0, - 1);
}
backSpace();

// Clear all Inputs
clearBtn.addEventListener('click', ()=> {
    clearCalculator();
})

// Backspace
backBtn.addEventListener('click', ()=> {
    backSpace();
})

// For Operators and Number Inputs
btnSpread.forEach((button, i) => {
    button.addEventListener("click", () => {

        let value = btns[i].innerHTML;

        if(resultBox.innerHTML.length<=8)
        {
            if (resultBox.innerHTML == "0")
            {
                resultBox.innerHTML = "";
                resultBox.innerHTML += value;
                isNumber = true;
            }
            else if (value == '.' && !isDot && isNumber == true)
            {
                isDot = true;
                resultBox.innerHTML += value;
            }
            else if ((value == '+') || (value == '-') || (value == '*') || (value == '/') || (value == '%') && (isOperator))
            {
                resultBox.innerHTML += value;
                isOperator = false;
                isNumber = true;
                isDot = false;
            }
            else if (value >= '0' && value <= 9 && isNumber)
            {
                resultBox.innerHTML += value;
                isOperator = true;
            }
        }
        else
        {
            alert("Error: Input size restricted to 9 digits")
        }

    });
});

// Function to Evaluate Strings
function evaluate(fn) {
    return new Function('return ' + fn)();
}

// To calculate All Input
total.addEventListener('click', ()=> {
    let allInputs = resultBox.innerHTML;
    let res = evaluate(allInputs);
    if(res.toString().length<=8)
        resultBox.innerHTML = res
    else
       alert("Error: Output size restricted to 9 digits")
    isNumber = false;
})
