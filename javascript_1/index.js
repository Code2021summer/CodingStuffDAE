document.getElementById("clicker").innerText = "CLICK ME";
console.log("JavaScript is working!");
let clicks = 0;
const clicker = document.getElementById('clicker');
clicker.addEventListener('click', function() {
    //window.alert("the clicker clicks");
    clicks = clicks + 1;
    //window.alert(clicks);
    if (clicks==5) {
        document.getElementById("clickCount").innerText = "YO YOU DID IT"; 
        clicker.onclick = function(){
            window.location.href = "https://shattereddisk.github.io/rickroll/rickroll.mp4";
        };
    } 
    if (clicks == 1) {
        document.getElementById("clickCount").innerText = clicks + " click";
    }
    else
        document.getElementById("clickCount").innerText = clicks + " clicks";
});

