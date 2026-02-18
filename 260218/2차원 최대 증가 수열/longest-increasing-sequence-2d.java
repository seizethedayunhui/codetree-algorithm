import java.util.*;

public class Main {

    public static int MIN_V = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N, M;
        N = sc.nextInt();
        M = sc.nextInt();

        int[][] mat = new int[N][M];
        int[][] dp = new int[N][M];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                mat[i][j] = sc.nextInt();
                dp[i][j] = MIN_V;
            }
        }

        dp[0][0] = 1;
        int ans = MIN_V;

        for(int x = 0; x < N; x++){
            for(int y = 0; y < M; y++){

                for(int r = 0; r < x; r++){
                    for(int c = 0; c < y; c++){

                        // if((r == x && c == y) || (r == x - 1 && c == y) || (r == x && c == y-1)){
                        //     continue;
                        // }

                        if( mat[x][y] > mat[r][c] && dp[r][c] != MIN_V){
                            dp[x][y] = Math.max(dp[x][y], dp[r][c] + 1);
                        }
                    }
                }

                ans = Math.max(ans, dp[x][y]);

            }
        }

        System.out.println(ans);
    }
}
