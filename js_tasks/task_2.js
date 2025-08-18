function sumOfString(str){
    str_arr=str.trim().split(",");
    let sum = 0;
    for (let i = 0; i < str_arr.length; i++) {
        str_arr[i] = str_arr[i].trim();
        sum+=Number(str_arr[i]);
    }
    return sum;
}

let str =  "1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"
console.log("Sum of numbers in the string is: " + sumOfString(str));