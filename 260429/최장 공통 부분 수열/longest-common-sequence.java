import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        // Please write your code here.

        int N = A.length();
        int M = B.length();

        int[][] dp = new int[N+1][M+1];

        for(int i = 0; i < N+1; i++){
            dp[i][0] = 0;
        }

        for(int i = 0; i < M+1; i++){
            dp[0][i] = 0;
        }

        for(int i = 1; i < N+1; i++){
            for(int j = 1; j < M+1; j++){

                if (A.charAt(i-1) == B.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        int ans = dp[N][M];

        System.out.println(ans);
    }
}