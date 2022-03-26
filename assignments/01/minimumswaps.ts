// idea. Look at the index position and compare the indexpositon with the value
function minimumSwaps(arr) {
  let ans = 0;
  for (let i = 0; i < arr.length - 1; ) {
    if (arr[i] == i + 1) {
      i++;
    } else {
      let temp = arr[i];
      arr[i] = arr[temp- 1];
      arr[temp - 1] = temp;
      console.log(arr) // the array gets sorted
      ans++;
    }
  }

  return ans;
}

// Big o => O(n) its linear complexity
let usorted = [1,4,3,2]
let expected = 1 // swapping 4 and 2

console.log(minimumSwaps(usorted))