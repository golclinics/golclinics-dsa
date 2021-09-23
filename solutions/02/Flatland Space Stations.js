// Complete the flatlandSpaceStations function below.
function flatlandSpaceStations(n, c) {
    let d=[],max=0;
    for(let i=0;i<n;i++){
    let m=n;
    for(let j=0;j<c.length;j++){
        let dist = Math.abs(i-c[j]);
        m=dist<m?dist:m;
    }  
    console.log('min for',i,'is',m)
    max=m>max?m:max;
  }
  return max;
}
