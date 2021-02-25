import java.util.HashSet;

// Hash set
public class IsValidString {

    public static void main(String args[]) {
        System.out.println(isValid("aabbcd")); //abcc = YES, aabbccddeefghi = NO ,abcdefghhgfedecba = yes, aabbcd = NO
    }

    // Complete the isValid function below.
    static String isValid(String s) {
        char[] ca = s.toCharArray();
        HashSet<Character> hs = new HashSet<>();
        for (char c : ca) {
            if (hs.contains(c)) {

            } else {
                hs.add(c);
            }
            System.out.println(hs.size());
        }

        if (s.length() % hs.size() == 0 || s.length() % hs.size() == 1) {
            return "YES";
        } else {
            return "NO";
        }
    }

}
