package array;

/*
* Hour Glass Problem
* */
public class ArrayDS {
    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        //step 1,get the length of the rows and columns
        int row = arr.length;
        int col = arr[0].length;
        int max_hour_glass = Integer.MIN_VALUE;
        for(int i=0;i<row-2;i++){
            for(int j=0;j<col-2;j++){
                int current_hour_glass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
                max_hour_glass = Math.max(max_hour_glass,current_hour_glass);
            }
        }

        return max_hour_glass;

    }

}
