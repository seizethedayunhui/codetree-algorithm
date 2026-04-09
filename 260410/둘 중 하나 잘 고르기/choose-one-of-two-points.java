import java.util.*;
public class Main {
    public static int MIN_V = Integer.MIN_VALUE;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] reds = new int[2*n];
        int[] blues = new int[2*n];

        for (int i = 0; i < 2 * n; i++) {
            int red = sc.nextInt();
            int blue = sc.nextInt();
            reds[i] = red;
            blues[i] = blue;
        }
    
        int[][] dp = new int[2*n + 1][n+1];
        for(int i = 0; i < 2 * n; i++){
            for(int j = 0; j < n+1; j++){
                dp[i][j] = MIN_V;
            }
        }

        dp[0][0] = 0;

        for(int i = 1; i < 2 * n +1; i++){
            for(int j = 0; j < n + 1; j++){
                if (j == 0){
                    dp[i][j] = dp[i-1][j] + blues[i-1];
                } else{
                    dp[i][j] = Math.max(
                        dp[i-1][j-1] + reds[i-1],
                        dp[i-1][j] + blues[i-1]
                    );
                }
            }
        }

        int answer = dp[2*n][n];
        System.out.println(answer);
    }
}