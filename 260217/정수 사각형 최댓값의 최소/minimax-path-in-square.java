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
        for(int r=1; r < N; r++){
            dp[r][0] = Math.max(dp[r-1][0], mat[r][0]);
        }

        for(int c =1; c < N; c++){
            dp[0][c] = Math.max(dp[0][c-1], mat[0][c]);
        }

        for(int x = 1; x < N; x++){
            for(int y = 1; y < N; y++){

                dp[x][y] = Math.max(
                    Math.min(dp[x-1][y], dp[x][y-1]),
                    mat[x][y]
                );
            }
        }

        int ans = dp[N-1][N-1];
        System.out.println(ans);
    }
}