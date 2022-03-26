package array;

public class ArrayManipulation {
    static long arrayManipulation(int n, int[][] queries) {

        long[] result = new long[n];
        int length = queries.length;
        long max = Long.MIN_VALUE;

        for(int i=0;i<length;i++){
            int start = queries[i][0]-1; //1-indexed
            int end = queries[i][1]-1;
            int add = queries[i][2];
            result[start] += add;
            if(end+1<n){
                result[end+1] -= add;
            }
        }
        for(int i=1;i<n;i++){
            result[i] += result[i-1];
            max = Math.max(max,result[i]);
        }
        return max;
    }
}
