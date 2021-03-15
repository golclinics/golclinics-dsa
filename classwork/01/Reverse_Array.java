public class Reverse_Array {

    public static void main(String[] args){

        int[] arr = {1, 2, 4, 6, 7, 3, 5, 10, 17};

        for(int i = 0;i< arr.length/2;i++){

            int temp = arr[i];
            arr[i] = arr[arr.length-i-1];
            arr[arr.length-i-1] = temp;
        }
        // enhanced for loop is a simpler way to do this same thing. (The colon in the syntax can be read as "in.")
        for(int item : arr){
            System.out.println(item);
        }
    }

}
