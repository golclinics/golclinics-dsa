//  Creating a deep copy of an array, write a function `deepCopy`
// Reverse an array with O(1) space complexity (_in-place reverse_)

function deepCopy(arr) {
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    [arr[i], arr[arr.length - 1 - i]] = [arr[arr.length - 1 - i], arr[i]];
  }
  return console.log(arr);
}

deepCopy([1, 2, 3, 4]);

// the algorithm has a time complexity of 0(n) and a space complexity of o(1)