import java.util.*;

public class MakingAnagrams {

    public static void main(String args[]) {
        System.out.println(makeAnagram("cccd", "ddd"));
    }

    // Complete the makeAnagram function below : returns minimum number of character deletions required to make the two strings anagrams
    static int makeAnagram(String a, String b) {
        char[] chars = a.toCharArray();
        ArrayList<Character> charList1 = new ArrayList<>();
        for (char i : chars) {
            charList1.add(i);
        }

        char[] chars2 = b.toCharArray();
        ArrayList<Character> charList2 = new ArrayList<>();
        for (char i : chars2) {
            charList2.add(i);
        }


        int deletions = 0, counter = 0, len1 = a.length(), len2 = b.length();

        for (Character value : charList1) {
            for (Character character : charList2) {
                if (String.valueOf(value).equals(String.valueOf(character))) {
                    charList2.remove(character);
                    counter += 1;
                    break;
                }
            }
        }

        deletions = (len1 + len2) - counter * 2;

        return deletions;
    }
}