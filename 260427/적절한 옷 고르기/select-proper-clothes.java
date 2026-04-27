import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] s = new int[n+1];
        int[] e = new int[n+1];
        int[] v = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            s[i] = sc.nextInt();
            e[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }

        int[][] dp = new int[m+1][n+1];

        for(int i = 0; i < m+1; i++){
            for(int j = 0; j < n+1; j++){
                dp[i][j] = Integer.MIN_VALUE;
            }
        }

        for(int i = 1; i < n+1; i++){
            if ( s[i] <= 1 && e[i] >= 1 ){
                dp[1][i] = 0;
            }
        }

        for(int i = 2; i < m+1; i++){
            for(int j = 1; j < n+1; j++){

                // check possible clothes
                if (s[j] > i || e[j] < i) continue;

                for(int k = 1; k < n+1; k++){
                    
                    if (dp[i-1][k] == Integer.MIN_VALUE) continue;

                    int statisfac = Math.abs(v[j]-v[k]);
                    dp[i][j] = Math.max(dp[i-1][k] + statisfac, dp[i][j]);

                }
            }
        }

        int ans = Integer.MIN_VALUE;

        for(int i = 1; i < n+1; i++){
            ans = Math.max(dp[m][i], ans);
        }

        System.out.println(ans);

    }
}