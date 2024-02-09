//console.log("Hello World")
const timer = document.getElementById('displaytimer')
//console.log(timer.textContent)
const inputTag = document.getElementById('timer')

setInterval(myTimer, 1000);
//There are 1000 milliseconds in one second.

t=0
function myTimer () {
    t+=1
    timer.innerHTML ="<b>Timer: " +t+" seconds</b>"
    inputTag.value = t
}
