const maxHourglassSum = (array) => {
  let sums = [];
  // the last two rows and columns are cannot make an hourglass
  for (let i = 0; i < array.length - 2; i++) {
    for (let j = 0; j < array[i].length - 2; j++) {
      let sum =
        array[i][j] +
        array[i][j + 1] +
        array[i][j + 2] +
        array[i + 1][j + 1] +
        array[i + 2][j] +
        array[i + 2][j + 1] +
        array[i + 2][j + 2];
      sums.push(sum);
    }
  }
  return Math.max(...sums); //
};

// big o(n*n + o(n)) most deminant
// O(n^2)

let numbers = [
  [-9, -9, 9, 1, 1, 1],
  [0, -9, 0, 1, 1, 1],
  [-9, -9, -9, 1, 2, 3],
  [-0, -0, 9, -2, 1, 1],
  [-0, -0, 9, 2, 4, 1],
];

const asn = maxHourglassSum(numbers);
console.log(asn);
