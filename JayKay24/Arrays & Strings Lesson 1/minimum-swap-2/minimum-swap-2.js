// Hackerrank did not support Typescript for this challenge

/**
 * Returns minimum number of swaps required to sort the arrray in ascending
 * order
 * @param {object} arr - an unordered array of integers
 * @returns {number} minimum number of swaps to order the array
 * in ascending order
 */
function minimumSwaps(arr) {
  let minSwaps = 0;

  for (let i = 0; i < arr.length; i++) {
    while (arr[i] !== arr[arr[i] - 1]) {
      swap(arr, i, arr[i] - 1);
      minSwaps++;
    }
  }

  return minSwaps;
}

function swap(arr, idx1, idx2) {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const integers = [7, 1, 3, 2, 4, 5, 6];
console.log(minimumSwaps(integers)); // 5
