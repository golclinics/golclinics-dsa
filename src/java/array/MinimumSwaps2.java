package array;

public class MinimumSwaps2 {
    static int minimumSwaps(int[] arr) {
        int min_index=0;
        int min = arr[0];
        int swaps = 0;
        //update min index and min value
        for(int i=1;i<arr.length;i++){
            if(arr[i]<min){
                min_index = i;
                min = arr[i];
            }
        }
        //swap as long as minimum index is not equal to 0
        if(min_index != 0){
            int temp  = arr[0];
            arr[0] = arr[min_index];
            arr[min_index] = temp;
            swaps++;
        }
        for(int j=1;j<arr.length-1;j++){
            //calculate the position
            int pos = arr[j]-arr[0];
            while(arr[pos] != arr[j]){
                int temp = arr[pos];
                arr[pos] = arr[j];
                arr[j] = temp;
                swaps++;
                pos = arr[j]-arr[0];
            }
            j = pos;
        }
        return swaps;
    }
}
