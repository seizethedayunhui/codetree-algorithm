import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

    
        long[][] dp = new long[n + 1][10];
        long mod = 1000000007L; 
    
        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 10; j++) { 
                for (int k = 0; k < 10; k++) { 
                    
                    if (Math.abs(j - k) == 1) {
                    
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % mod;
                    }
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < 10; i++) {
            ans = (ans + dp[n][i]) % mod;
        }
        
        System.out.println(ans);
    }
}