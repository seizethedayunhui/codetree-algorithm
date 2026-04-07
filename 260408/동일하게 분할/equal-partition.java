import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n+1];

        int m = 0;
        for(int i = 1; i < n+1; i++){
            arr[i] = sc.nextInt();
            m += arr[i];
        }
        
        boolean[][] dp = new boolean[n+1][m + 1];
        dp[0][0] = true;

        for(int i = 1; i < n+1; i++){
            for(int j = 0; j < m+1; j++){
                
                if ((j >= arr[i]) && dp[i-1][j-arr[i]]){
                    dp[i][j] = true;
                }

                if (dp[i-1][j]){
                    dp[i][j] = true;
                }
            }
        }

        int subSum = 0;
        for(int j = 0; j < m+1; j++){

            if (dp[n][j] && (m - j == j)){
                System.out.println("Yes");
                return;
            }
        }

        System.out.println("No");
        return;
    }
}