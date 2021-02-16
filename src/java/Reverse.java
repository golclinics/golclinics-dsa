import java.util.Arrays;

public class Reverse {
    //O(n)
    public static int[] reverse(int[] A){
        int reverse_index = 0;
        int[] reversed_array = new int [A.length];
        for (int i=A.length - 1;i>=0;i--){
            reversed_array[reverse_index] = A[i];
            reverse_index++;
        }
        return reversed_array;
    }
    //O(1)
    public static int[] reverse1(int[]A){
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

    public static void main(String[] args) {
        int[] A = {1,2,5,6};
        //in this case assuming reverse point is 2
        System.out.println(Arrays.toString(reverse1(A)));
    }
}
