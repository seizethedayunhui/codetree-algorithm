import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

       int N = sc.nextInt();
       int[][] mat = new int[N][N];
       int[][] dp = new int[N][N];

       for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            mat[i][j] = sc.nextInt();
        }   
       }

       dp[0][0] = mat[0][0];

       for(int col= 1; col < N; col++){
            dp[0][col] = Math.min(dp[0][col-1], mat[0][col]);
       }

       for(int row = 1; row < N; row++){
            dp[row][0] = Math.min(dp[row-1][0], mat[row][0]);
       }

       for(int i = 1; i < N; i++){
        for(int j = 1; j < N; j++){
            if ((i == N-1) && (j == N-1)){
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            } else{
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
       }

       int ans = dp[N-1][N-1];
       System.out.println(ans);
    }
}