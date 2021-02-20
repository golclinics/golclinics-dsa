const biggerIsGreater = (w) => {
  w = w.split("");  // split by characters
  let i = w.length - 1;

  while (i > 0 && w[i - 1] >= w[i]) i--;

   if (i <= 0) return "no answer";

  let j = w.length - 1;

  // bigger is greater> we swap big and small
  while (w[j] <= w[i - 1]) j--;
    w = swap(w, i-1, j)

  j = w.length - 1;
  while (i < j) {
    w = swap(w, i, j)
    i++;
    j--;
  }
  return w.join(""); 
}

const swap = (array, i, j) => {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
  return array
}

// all test cases

console.log(
biggerIsGreater("hefg") // only swap fg
)

console.log(
biggerIsGreater("ab") // only swap ab
)


console.log(
biggerIsGreater("bb") // no answer. no greater
)



console.log(
biggerIsGreater("dhck") // only swap  dhck
)


console.log(
biggerIsGreater("dkhc") // only swap hcdk
)
