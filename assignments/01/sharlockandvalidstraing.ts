function isValid(s) {
  let counter = {};
  let freq = {};
  s = s.split("");
  // count of occurrences of characters
  s.forEach((char) => {
    counter[char] = counter[char] || 0;
    counter[char]++;
  });

  // count the frequency of those occurence counts,
  // map
  let counterkeys = Object.getOwnPropertyNames(counter);
  counterkeys.forEach((k) => {
    freq[counter[k]] = freq[counter[k]] || 0;
    freq[counter[k]]++;
  });

  let freqMap = Object.keys(freq).map(Number);

  //if there is only one frequency, it's valid
  if (freqMap.length === 1) {
    return "Is valid string";
  }

  // If not a single frequency string
  let twoOccurrence = freqMap.length === 2;
  let [a, b] = freqMap; // some destructuring

  // frequency occurs only once
  let oneOccurence = freq[a] === 1 || freq[b] === 1;

  // the difference is a single character
  // e.g. abbcc
  let single = (freq[a] === 1 && a === 1) || (freq[b] === 1 && b === 1);

  // differing frequency is exactly 1 more than others
  // e.g. true if aaabbcc, false if abbcc
  let diffOfOne = (freq[a] === 1 ? a - b : b - a) === 1;

  if ((single || diffOfOne) && twoOccurrence && oneOccurence) {
    return "Is valid String";
  }
  return "Not Valid";
}

let s = "abcc";
console.log(
  isValid(s) // s is valid have frequency of one for all strings
);

let s2 = "abcdefghhgfedecba";
console.log(
  isValid(s2) // s is valid have frequency of one for all strings
);
