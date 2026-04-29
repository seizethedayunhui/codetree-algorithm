import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] data = new int[N+1][4];
        for (int i = 1; i < N+1; i++) {
            data[i][1] = sc.nextInt();
            data[i][2] = sc.nextInt();
            data[i][3] = sc.nextInt();
        }
        // Please write your code here.

        int[][] dp = new int[N+1][4];
        for(int i = 1; i < 4; i++){
            dp[1][i] = data[1][i];
        }

        for(int i = 2; i < N+1; i++){
            for(int j = 1; j < 4; j++){
                for(int k = 1; k < 4; k++){
                    if (j==k) continue;

                    dp[i][j] = Math.max(dp[i][j], dp[i-1][k] + data[i][j]);
                }
            }
        }

        int ans = Integer.MIN_VALUE;
        for(int i = 1; i < 4; i++){
            ans = Math.max(ans, dp[N][i]);
        }

        System.out.println(ans);
    }
}