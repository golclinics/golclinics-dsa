import java.io.*;
import java.util.*;

public class array_2d {



        // Complete the hourglassSum function below.
       public static int hourglassSum(int[][] arr) {

            int rows = arr.length;

            int columns =arr[0].length;

            int max_hourglass = Integer.MIN_VALUE;

            for(int i = 0; i<rows-2; i++){

                for(int j =0; j<columns-2; j++){

                    int current_hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
                    max_hourglass = Math.max(max_hourglass,current_hourglass_sum);
                }
            }
            return max_hourglass;
        }


        public static void main(String[] args) throws IOException {


            int[][] arr = new int[6][6];
            System.out.println(hourglassSum(arr));



    }



}


