 
var operators = ['+','-','*','/','%'];
var input_value;
var operator;

var input_array = [];

function display(val)
{
   
   if (document.getElementById("result").value.length <=9)
   { 
       document.getElementById("result").value+=val;
   }
   else if (document.getElementById("result").value.length >=9 ) 
   {
    alert('This calculator will not accept more than 9 digits, so clear 1 digit');
   }
   input_array[0]  = document.getElementById("result").value;
};


function cls()
{
    document.getElementById("result").value = "";
    document.getElementById("display2").value = "";
};

function calculate()
{
    input_value  = input_value + input_array[0];
    let x = input_value;
    let y = eval(x);
    if ( y.toString().length > 9)
    {
       alert('The output is more than 9 digits');
       document.getElementById("result").value = "";
       document.getElementById("display2").value = "";

    }
    else 
    {
      document.getElementById("result").value = y;
      input_array =[];
    }
};


function clearlastelement()
{
   var val1 = document.getElementById("result").value;
   document.getElementById("result").value = val1.substr(0,val1.length-1);
};

function display_ops(val)
{
   if (input_array.length == 0)
   {
       alert('Please dont enter operator first or dont enter operator multiple times, clear screen and enter numbers');
   }
   else 
   {   operator = val;
       input_value = input_array[0]+operator;
       input_array=[];
       document.getElementById("display2").value  = input_value;
       document.getElementById("result").value = "";
   } 
};