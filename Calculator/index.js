//Calculator program

const display = document.getElementById('display');                    //gets information of the display from index.html

function appendToDisplay(input){                                       
    display.value += input;                                            //makes the given input to show on the display

}

function clearDisplay(){
    display.value = "";                                                //Makes the button C to clear the display

}

function calculate(){
    try{                                                               //Checks if the code works
        display.value = eval(display.value);                           //Evaluates the value and gives an output
    }
    catch(error){                                                      //Displays error if cant calculate the given input
        display.value = "Error";
    }

}