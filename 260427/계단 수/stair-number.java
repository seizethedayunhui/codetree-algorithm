import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.

        int[][] dp = new int[n+1][10];

        for(int i = 1; i < 10; i++){
            dp[1][i] = 1;
        }

        for(int i = 2; i < n+1; i++){
            for(int j = 0; j < 10; j++){
                for(int k = 0; k < 10; k++){

                    if(Math.abs(j-k) == 1){
                        dp[i][j] += dp[i-1][k];
                    }
                }
            }
        }

        int ans = 0;
        for(int i = 0; i < 10; i++){
            ans += dp[n][i];
        }
        ans = ans % ((int) Math.pow(10, 9) + 7);
        System.out.println(ans);
    }
}