// use strict

const arrayleftrotation = (arr, n) => {
  //arr > the array
  // n > number of left rotation
  for (let d = 0; d < n; d++) {
    let temp = arr[0];
    for (let i = 0; i < arr.length - 1; i++) {
      arr[i] = arr[i + 1];
    }
    arr[arr.length - 1] = temp;
  }
  return arr;
};
// The function has two nested 4 loops.
// Big 0(n^2) ==> bad performace for a very large input
let testarray = [1, 2, 3, 4]; // for one location
let expectedresult = [2, 3, 4, 1];
let a = arrayleftrotation(testarray, 1);
console.log(a);

// For 4 rotations
let testarraytwo = [1, 2, 3, 4, 5];
let expectedasn = [5, 1, 2, 3, 4];
let b = arrayleftrotation(testarraytwo, 4);
console.log(b);

// TODO: How can I improve this solution to more efficient?

