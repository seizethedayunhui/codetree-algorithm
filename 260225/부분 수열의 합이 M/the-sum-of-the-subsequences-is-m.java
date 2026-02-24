import java.util.*;

public class Main {

    public static int MAX_VALUE =10000;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] coin = new int[N];
        int[] dp = new int[M+1];

        for(int i = 0; i < N; i++){
            coin[i] = sc.nextInt();
        }

        for(int j = 0; j < M+1; j++){
            dp[j] = MAX_VALUE;
        
        }

        dp[0] = 0;

        for(int k = 0; k < N; k++){
            for(int l = M; l >= 0; l--){
                if (l >= coin[k]){
                    dp[l] = Math.min(dp[l], dp[l-coin[k]]+1);
                }
            }

        }

        // for(int m = 0; m < M+1; m++){
        //     System.out.print(dp[m]+ " ");
        // }

        int ans = dp[M];

        if (ans >= MAX_VALUE){
            ans = -1;
        }

        System.out.println(ans);
    }
}