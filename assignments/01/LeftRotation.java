public class LeftRotation {

    public static void main(String args[]) {
        System.out.println();
        int a[] = {1, 2, 3, 4, 5};
        rotLeft(a, 4);
    }

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {

        int[] b = a;
        for (int i = 0; i < a.length; i++) {
            if(a[i]<1 || a[1]>1000000){
                return b;
            }
        }

        //constraints
        int n = a.length;
        if (n < 1 || n > 100000)
            return a;

        if (d < 1 || d > n)
            return a;

        for (int x = 0; x < d; x++) {
            int temp = 0;
            //single shift
            for (int i = 0; i < a.length; i++) {
                if (i == 0) {
                    temp = a[0];
                    a[0] = a[1];
                } else if (i == a.length - 1) {
                    a[a.length - 1] = temp;
                } else {
                    a[i] = a[i + 1];
                }
            }
        }

        return a;
    }
}