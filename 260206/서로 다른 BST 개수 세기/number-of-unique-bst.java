import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] dp = new int[N+1];

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i < N+1; i++){

            int sum = 0;
            for(int k = 0; k < i; k++){
                sum += (dp[i-(k+1)] * dp[k]);
            }

            dp[i] = sum;
        }

        System.out.println(dp[N]);
    }
}