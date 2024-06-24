// Complete the hourglassSum function below.
function hourglassSum(arr) {
    let i=0,j=0,sum= 0,highestSum=-63;

    while(i<4){
        while(j<4){
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            highestSum = sum>highestSum?sum:highestSum;
            j++;
        }
    j=0;i++;
  }
  return highestSum;
}
