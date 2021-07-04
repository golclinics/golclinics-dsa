function nonDivisibleSubset(k, s) {
  // Write your code here
  let values = [];
  let result = 0;

  s.reduce((target, item, index) => {
    values[item % k] += 1;

    return target;
  });
 
   let length = (k + 1) / 2 - 1;
    for (let i = 0; i < length ;i++) 
      result += Math.max(values[i], values[k - i]);
    } 

  return result;
}

// TODO: think of a different solution
// Solution: not working
