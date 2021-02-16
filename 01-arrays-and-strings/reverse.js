

// O(n) space complexity
function reverse(A) {
    let copyA = new Array(A.length); // size 0 -> space complexity O(n)

    let j = 0;
    for (let i = A.length - 1; i >= 0; i--) {
        // copyA.push(A[i]); // not efficient
        copyA[j] = A[i];
        j++;
    }

    return copyA;
}

// O(1) space complexity
// ...

// TBD


// tests
let a = [1, 4, 5, 6];
console.log(reverse(a));
