function alternatingCharacters(s) {
  let deletions = 0;
  for (let i = 0; i < s.length - 1; i++) {
    if (s[i] === s[i + 1]) deletions++;
  }

  return deletions;
}

//Note: strings are arrays ? why did i even split
//this was a simple one
//Big o notation of 0(n)

let stringa = "BBBBB"; // 4 deletions
let stringb = "AAAA"; // 3 deletions
let stringc = "ABABABAB"; // 0 deletion

console.log(alternatingCharacters(stringa));

console.log(alternatingCharacters(stringb));

console.log(alternatingCharacters(stringc));
