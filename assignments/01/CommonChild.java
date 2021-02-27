public class CommonChild {
    public static void main(String args[]) {
        System.out.println(commonChild("NOHARAAA","SHINCHAN"));
    }

    // Complete the isValid function below.
    static int commonChild(String s1, String s2) {


        char[] cars1 = s1.toCharArray();
        char[] cars2 = s2.toCharArray();

        int k = 0, counter = 0;
        for (int i = 0; i < cars1.length; i++) {
            for (int j = k; j < cars2.length; j++) {
                if (cars1[i] == cars2[j]) {
                    counter += 1;
                    k=j+1;
                    break;
                }
            }
        }

        return counter;
    }
}