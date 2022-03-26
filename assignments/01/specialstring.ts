function substrCount(n, s) {
  let history = [];
  let historyCount = 0;

  // historyItem = [current, occurrence]
  // if seen again the counter is incremented
  let seentimes = [s[0], 1];

  let pcount = 0;

  for (let i = 1; i < n; i++)
    if (s[i] == seentimes[0]) seentimes[1]++;
    else {
      // Calcuate all strings that can be formed with the same character
      // Count total substrings  -> n * (n + 1) / 2 for
      pcount += (seentimes[1] * (seentimes[1] + 1)) / 2;

      if (historyCount == 2) {
        // Calcuate all strings that can be formed with the same character except middle character
        if (history[0][0] == seentimes[0] && history[1][1] == 1)
          pcount += Math.min(history[0][1], seentimes[1]);
        history.shift(); // remove the first element. not good O(n). but the size is one
        historyCount--; // decrement
      }

      history.push(seentimes); // O(n)
      historyCount++;
      seentimes = [s[i], 1];
    }

  pcount += (seentimes[1] * (seentimes[1] + 1)) / 2;

  if (historyCount == 2)
    if (history[0][0] == seentimes[0] && history[1][1] == 1)
      pcount += Math.min(history[0][1], seentimes[1]);

  return pcount;
}

// test 1
let n = 1;
let s = "aaa";

// test 1
let n1 = 6;
let s2 = "aaaaabb";

console.log(substrCount(n, s));

console.log(substrCount(n1, s2));
