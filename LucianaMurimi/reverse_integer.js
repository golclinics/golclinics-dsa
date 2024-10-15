//1. STRING
//-----------
//Write a program that takes an integer as input and return an integer with reversed digit ordering.

//For example

//For input 500, the program should return 5. 
//For input -56, the program should return -65. 
//For input -90, the program should return -9. 
//For input 91, the program should return 19. 

function reverseInteger(n){
    let str = n.toString();

    if(n < 0){
        return parseInt('-' + str.slice(1).split('').reverse().join(''));
    }else{
        return parseInt(str.split('').reverse().join(''));
    }
}

// Test cases
console.log(reverseInteger(500));   
console.log(reverseInteger(-56));   
console.log(reverseInteger(-90));  
console.log(reverseInteger(91));    