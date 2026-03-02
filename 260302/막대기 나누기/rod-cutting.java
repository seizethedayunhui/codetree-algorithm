import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] money = new int[N];
        for(int i = 0; i < N; i++){
            money[i] = sc.nextInt();
        }

        int[] dp = new int[N+1];
        dp[0] = 0;

        for(int j = 0; j < N+1; j++){
            for(int k = 0; k < N; k++){
                if( j >= k+1){
                    dp[j] = Math.max(dp[j], dp[j-k-1] + money[k]);
                }
            }
        }

        int ans = dp[N];
        System.out.println(ans);
    }
}