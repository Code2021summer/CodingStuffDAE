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

const cells = document.querySelectorAll(".cell");
const statusText = document.querySelector("#statusText");
const restartBtn = document.querySelector("#restartBtn");
const winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];
let options = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let running = false;
initializeGame();
function initializeGame(){
    cells.forEach(cell => cell.addEventListener("click", cellClicked));
    restartBtn.addEventListener("click", restartGame);
    statusText.textContent = "${currentPlayer}'s turn"
    //exactly 10 minutes in https://www.youtube.com/watch?v=AnmwHjpEhtA
}
function cellClicked(){

}
function updateCell(cell, index){

}
function changePlayer(){

}
function checkWinner(){

}
function restartGame(){

}