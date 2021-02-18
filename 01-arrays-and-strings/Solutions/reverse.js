function swap(A, i, j){
    let temp = A[i];

    A[i] = A[j];
    A[j] = temp;
}

// A is an array
function reverse(A) {
    // Calculate the midpoint of the array
    let array_size = A.length;
    let mid_point = array_size / 2;

    for(let i = 0; i < mid_point; ++i){
        swap(A, i, array_size - i - 1)
    }

    return A;
}

// Tests
console.log(reverse([1, 2, 3, 4, 5]));
