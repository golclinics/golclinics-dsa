// s1, s2 two equal length strings
// the constrans are up to a maximumu of 5000 characters
// occurence of similar character on both string
// count the length of the pairs
// rearrage in not allowed
function commonChild(s1, s2) {
  if (s1.length !== s2.length) {
    return "not equal";
  }
  let cache = [];

  for (let element of s1) {
    let index = element.charCodeAt(0) - 97;
    cache[index] = cache[index] || 0;
    cache[index] += 1;
  }

  for (let element of s1) {
    let index = element.charCodeAt(0) - 97;
    cache[index] = cache[index] || 0;
    cache[index] += 1;
  }

  return cache.reduce((a, b) => {
    if (b == 2) {
      return a++;
    }
    return a;
  });
}

// two separate loops improves the big0 of the algorithm.
// Some pattern is becoming visible. when working with two array that involves
// comparison of its element work on the first array first save in the cache. use
// the cache to work on the rest of the array.
// TODO improve other solution with big0 of O(n^2)
//
//
// big o is > O(3(n)) => drop constant => O(n)
console.log(commonChild("harry", "sally")); // expect two ay
