

function reverse(A) {
    let temp;
    let first = 0;
    let last = A.length -1;

    while(first < last){
        
        temp = A[first];
        A[first] = A[last];
        A[last] = temp;
        first++;
        last--;
    }
    return A
}

reverse([1,2,3,4,5,6,7])   //space o(1)
