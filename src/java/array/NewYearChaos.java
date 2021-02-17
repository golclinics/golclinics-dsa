package array;

public class NewYearChaos {
    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int swaps = 0;
        for(int i=q.length-1;i>=0;i--){
            if(q[i] != i+1){
                //test case 1,when a person can only bribe one person or move one unit
                if((i-1)>=0 && q[i-1] == i+1){
                    int temp = q[i-1];
                    q[i-1] = q[i];
                    q[i] = temp;
                    swaps++;
                }
                //test case 2,a person can only bribe two persons or move two units
                else if((i-2)>=0 && q[i-2] == i+1){
                    q[i-2] = q[i-1];
                    q[i-1]=q[i];
                    q[i] = q[i-2];
                    swaps += 2;
                }
                //test case 3,a person can bribe more than two persons or move more than two units
                else{
                    System.out.println("Too chaotic");
                    return;
                }
            }
        }
        System.out.println(swaps);

    }
}
