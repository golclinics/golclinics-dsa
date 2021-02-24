const { CustomStack } = require("./stackimpelemetation");

const math = (s) => {
  const calcstack = new CustomStack(); // store operators to stack
  let split = s.split("");
  let sum = Number.parseInt(s[0]); // use oerato
  for (let i = 0; i < split.length - 1; i++) {
    if (split[i] == "+" || split[i] == "-") {
      calcstack.push(split[i]);
    }
    if (!calcstack.isEmpty()) {
      let opertor = calcstack.pop();
      if (opertor == "+") {
        sum += Number.parseInt(split[i + 1]);
      } else if (opertor == "-") {
        sum -= Number.parseInt(split[i + 1]);
      }
    }
  }
  console.log(calcstack);
  return sum;
};

let s = "1+2+3-4";
console.log(math(s));
