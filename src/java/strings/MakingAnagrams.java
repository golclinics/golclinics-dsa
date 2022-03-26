package strings;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MakingAnagrams {
    static int makeAnagram(String a, String b) {
        HashMap<Character,Integer> count = new HashMap();

        for(char ch: a.toCharArray()){
            int ct = count.containsKey(ch)?count.get(ch) : 0;
            count.put(ch,(ct + 1));
        }
        for(char ch: b.toCharArray()){
            int ct = count.containsKey(ch) ? count.get(ch) : 0;
            count.put(ch,(ct - 1));
        }
        List<Integer> value = new ArrayList(count.values());
        int total = 0;
        for(int v: value){
            total += Math.abs(v);
        }
        return total;
    }
}
