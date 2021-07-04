function getTotalX(a, b) {
  // Write your code here
  let result = 0;
  let index = 1;
  let newa = a.splice(1, a.length); // remove a[0] element and saves it
  let betweensetscheck = a[0] * index <= b[0]; // check factors => 16
  while (betweensetscheck) {
    if (
      newa.every((item) => (a[0] * index) % item === 0) &&
      b.every((item) => item % (a[0] * index) === 0)
    ) {
      result++; // count factors
    }
    index++;
  }
  return result;
}


const a = [2, 4];
const b = [16, 32, 96];

console.log(getTotalX(a, b));


