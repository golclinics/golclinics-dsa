function flatlandSpaceStations(n, c) {
  //get distance for all stations
  const distances = []
  for (let i = 0; i < n; i++) {
   distances[i] = distaceFromSpaceStation(c,i);
  }
  console.log(distances)
  return Math.max(...distances); // 0n
}

const distaceFromSpaceStation = (c, i)=> {
  const distance = [];
  let temp = [];
  for (let j = 0; j < c.length; j++) {
    temp.push(Math.abs(c[j] - i)); // no negative distances
  }
  distance.push(Math.min(...temp));
  return distance;
}

//test

console.log(
flatlandSpaceStations(5, [0, 4])
)

// TODO: improve this solution in terms of space complexities.

