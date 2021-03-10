import java.util.*;

public class HashWarmUp {

    public static void main(String args[]) {
        System.out.println(wordFrequency("go as you go you you"));
    }

    static int wordFrequency(String S) {
        HashMap<String, Integer> count = new HashMap();
        int counter = 0;

        //count words per sentence
        String[] words = S.split(" ");

        for (String word : words) {
            if (!count.containsKey(word)) {
                count.put(word,1);
            } else {
                counter = count.get(word) + 1;
                count.put(word,counter);
            }
        }

        return Collections.max(count.values());
    }
}