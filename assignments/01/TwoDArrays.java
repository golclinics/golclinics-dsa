public class TwoDArrays {
    public static void main(String args[]) {
        int[][] arr = { {1,1,1,0,0,0},
                {0,1,0,0,0,0},
                {1,1,1,0,0,0},
                {0,0,2,4,4,0},
                {0,0,0,2,0,0},
                {0,0,1,2,4,0} };

        System.out.println(hourglassSum(arr));

    }

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        int biggestSum = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i + 1][j + 1] + arr[i+2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
                if (sum > biggestSum) {
                    biggestSum = sum;
                }
            }
        }
        return biggestSum;
    }
}
