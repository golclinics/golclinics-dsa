// O(1) space complexity
// ...

const reverse = (array) => {
  let temp;
  let firstindex = 0; // index 0
  let lastindex = array.length - 1; // last index
  while (firstindex < lastindex) {
    temp = array[firstindex];
    array[firstindex] = array[lastindex];
    array[lastindex] = temp;
    firstindex++;
    lastindex--;
  }
  return array;
};

// tests
let a = [1, 4, 5, 6];
console.log(reverse(a));
