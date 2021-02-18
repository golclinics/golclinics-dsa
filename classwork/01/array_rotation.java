import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class array_rotation {


    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {

        int n = a.length;

        int[] rotateArray = new int[n];

        for(int currentIndex = 0;currentIndex < n; currentIndex++){

            int newIndex = (currentIndex + n - d)%n;
            rotateArray[newIndex] = a[currentIndex];
        }

        return rotateArray;

    }


    public static void main(String[] args) throws IOException {


        int[] myArray = new int []{1,2,3};
        int[] result = rotLeft(myArray, 1);
        System.out.println(Arrays.toString(result));



    }
}
