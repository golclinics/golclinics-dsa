function reverseArray(A) {
    let left = 0;
    let right = A.length - 1;

    while (left < right) {
        [A[left], A[right]] = [A[right], A[left]];
        left++;
        right--;
    }
}
function reverseSentence(A) {
    function reverseSubArray(start, end) {
        while (start < end) {
            [A[start], A[end]] = [A[end], A[start]];
            start++;
            end--;
        }
    }
    reverseSubArray(0, A.length - 1);

    let start = 0;
    for (let end = 0; end <= A.length; end++) {
        if (end === A.length || A[end] === ' ') {
            reverseSubArray(start, end - 1);
            start = end + 1;
        }
    }
}

let A = [10, 5, 6, 9];
let B = ['t', 'h', 'i', 's', 'i', 's', ' ', 'g'];
reverseArray(A);
reverseSentence(B);
console.log(A); 
console.log(B); 



