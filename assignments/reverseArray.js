

function reverse(A){
    let output = [];

    //recursive function to reverse an array
    function reverseArray (arr){
      if (arr.length !== 0){
        output.push( arr.pop() );
        reverseArray( arr );
      }
    }
    
  
    reverseArray(A);
    return output;
}
reverse([1,2,5,6]) /// [ 6, 5, 2, 1 ]  O(n)
