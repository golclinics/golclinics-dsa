function minimumBribes(q) {
  let bribe = 0;
  let chaotic = false;
  for (let i = 0; i < q.length; i++) {
    if (q[i] - 1 > i + 2) {
      chaotic = true;
      break;
    }
    for (let j = Math.max(0, q[i] - 2); j < i; j++) {
      if (q[j] > q[i]) bribe++;
    }
  }

  if (chaotic === true) {
    console.log("Too chaotic");
  } else {
    console.log(bribe);
  }
}

let test1 = [2, 5, 1, 3, 4]; // expectedoutput => Too chotic
let test2 = [2, 1, 5, 3, 4];

minimumBribes(test1);
minimumBribes(test2);
