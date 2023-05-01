var nums = ""
var count = 0
function add() {
    count += 1
    x = document.getElementById("display_ip")
    nums += x.value
    if(count==2) {
        //alert(eval(nums))
        x.value = eval(nums)
        count = 0
        nums = ""
    }
    else {
        nums += "+"
        x.value = ''
    }
}

function clearDisp(){
    x = document.getElementById("display_ip")
    x.value = ''
}

function delvalue(){
    x = document.getElementById("display_ip")
    x.value = x.value.slice(0,-1)
}

function checkNum() {
    if (Number(x.value) == NaN ) alert("invalid input. use only numbers")
}

function appendDisp(val) {
    console.log(val)
    x = document.getElementById("display_ip")
    x.value += val
}