package array;

public class LeftRotation {
    /**
     O(n+m) Time Complexity
     O(n) Space Complexity
     **/

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {
        //grab the size
        int size = a.length;
        int[] rotated_array = new int[size];
        int rotated_index = d;
        int i=0;
        while(rotated_index < size){
            rotated_array[i] = a[rotated_index];
            i++;
            rotated_index++;
        }
        rotated_index = 0;
        while(rotated_index < d){
            rotated_array[i] = a[rotated_index];
            i++;
            rotated_index++;
        }
        return rotated_array;
    }
}
