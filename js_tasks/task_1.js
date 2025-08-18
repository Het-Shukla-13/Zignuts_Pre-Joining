function sumOfNumbers(str) {
    let sum = 0;
    for(let i = 0; i < str.length; i++) {
        if (str[i]>='0' && str[i]<='9') {
            sum += parseInt(str[i]);
        }
    }
    return sum;
}

let str = "foo8bar8cat1tc2";
console.log("Sum of numbers in the string is: " + sumOfNumbers(str));