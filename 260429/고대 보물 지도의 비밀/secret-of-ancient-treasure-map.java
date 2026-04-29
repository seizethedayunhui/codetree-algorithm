import java.util.Scanner;
public class Main {

    public static int MIN_V = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            arr[i] = sc.nextInt();
        }
        // Please write your code here.
        int[][] dp = new int[N+1][K+1];
        for(int i = 0; i < N+1; i++){
            for(int j = 0; j < K+1; j++){
                dp[i][j] = MIN_V;
            }
        }

        for(int i = 1; i < N+1; i++){

            if (arr[i] >= 0){
                dp[i][0] = Math.max(dp[i-1][0] + arr[i], arr[i]);
            }
            for(int j = 1; j < K+1; j++){

                    if(arr[i] >= 0){

                        if(dp[i-1][j] == MIN_V) continue;

                        dp[i][j] = Math.max(dp[i-1][j] + arr[i], arr[i]);
                    } else{
                        dp[i][j] = Math.max(dp[i-1][j-1] + arr[i], arr[i]);
                    }

            }
            
        }

        int ans = Integer.MIN_VALUE;
        for(int i = 1; i < N+1; i++){
            for(int j = 0; j < K+1; j++){
                ans = Math.max(ans, dp[i][j]);
            }
        }

        System.out.println(ans);
    }
}