function factorial(n){
    if(n<0){
        return "Factorial is not defined for negative numbers.";    
    }
    if(n===0){
        return 1;
    }
    return n*factorial(n - 1);
}

let num = 6;
console.log("Factorial of " + num + ": " + factorial(num));