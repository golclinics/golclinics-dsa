package array;

import java.util.Arrays;

public class Reverse {
    /*
    * Brute force solution
    *
    * */
    public static int[] reverseBruteForce(int[] A){
        int reverse_index = 0;
        int[] reversed_array = new int [A.length];
        for (int i=A.length - 1;i>=0;i--){
            reversed_array[reverse_index] = A[i];
            reverse_index++;
        }
        return reversed_array;
    }
    /*
    * Optimal solution
    * */
    public static int[] reverseOptimal(int[]A){
        int mid = (A.length + 1)/2;
        int i = 0;
        int j = A.length-1;
        while(i != mid){
            int temp = A[i];
            A[i] = A[j];
            A[j]=temp;
            i++;
            j--;
        }
        return A;
    }
}
