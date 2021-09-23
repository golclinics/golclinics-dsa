function reverse(A) {
    let reversedA = []
    for (let i = A.length - 1; i >= 0; i--) {
       reversedA.push(A[i]);
    }
    return reversedA;
}

let a = [1, 4, 5, 6];
console.log(reverse(a));
