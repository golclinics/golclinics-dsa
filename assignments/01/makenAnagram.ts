// anagram are words that can be formed by rearrangin the letters of another
// idea: convert the letters to numbers
// loop through the first word incrementing the occurence of of letters
// save the increment to a cache
// loop through the second string
// use the same cache. Like letter to cancel out
// new characters will have new letters.
// add up the index using an absolute function.
       // ignore the sign
function makeAnagram(a, b) {
  let anagram = [];

  for (let element of a) {
    let index = element.charCodeAt(0) - 97; // convert letters to numbers
    anagram[index] = anagram[index] || 0;
    anagram[index] += 1;
  }

  for (let element of b) {
    let index = element.charCodeAt(0) - 97; // getting the index of strings
    anagram[index] = anagram[index] || 0;
    anagram[index] -= 1;
  }
  //using the es6 function to reduce the arrays to a single valu
  return anagram.reduce((a, b) => Math.abs(a) + Math.abs(b));
}

let a = "cde";
let b = "dcf";

console.log(makeAnagram(a, b)); // expected is 2
