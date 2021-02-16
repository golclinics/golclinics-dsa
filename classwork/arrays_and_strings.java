public class arrays_and_strings {

    // reversing an array of integers
    public static void main(String[] args) {

        int[] array_reverse = {1, 2, 4, 6, 7, 3, 5, 10, 17};

        // loop through half of the array
        for (int i = 0; i < array_reverse.length / 2; i++) {

            //create a temp
            int t = array_reverse[i];
           array_reverse[i] = array_reverse[array_reverse.length - i - 1];

            array_reverse[array_reverse.length - i - 1] = t;


        for (int item : array_reverse) {
            System.out.println(item);
        }
    }
}
}
