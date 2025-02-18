//Random number generator program

const myButton = document.getElementById("myButton");  //saves the assigned variable data
const myLabel = document.getElementById("myLabel");    //saves the assigned variable data
const min = 1;                                         //Defines the minimum number
const max = 6;                                         //Defines the maximum number
let randomNum;                                         //Declares the random number

myButton.onclick = function(){
    randomNum = Math.floor(Math.random() * max) + min; //Generates a random number between 1 and 6
    myLabel.textContent = randomNum;
}
