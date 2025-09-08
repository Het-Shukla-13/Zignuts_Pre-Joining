function nthFibonacci(n) {
    if (n <= 1) return n;
    return nthFibonacci(n - 1) + nthFibonacci(n - 2);
}

function fibonacci_seq(n) {
    let fib_seq=[];
    for (let i = 0; i < n; i++) {
        fib_seq.push(nthFibonacci(i));
    }
    return fib_seq.toString();
}

function getFibSequence() {
    let n = parseInt(document.getElementById("number").value);
    if (n <= 0) {
        document.getElementById("output").style.display="block";
        document.getElementById("sequence").innerText="Please enter a positive integer.";
    }
    else{
        console.log(fibonacci_seq(n));
        document.getElementById("output").style.display="block";
        document.getElementById("sequence").innerText=fibonacci_seq(n);
    }
}