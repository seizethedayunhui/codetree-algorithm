import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] seq = new int[N];
        int[] dp = new int[M+1];

        for(int i = 0; i < N; i++){
            seq[i] = sc.nextInt();
        }

        int MAX_V = Integer.MIN_VALUE;

        for(int m = 0; m < M+1; m++){
            dp[m] = MAX_V;
        }

        dp[0] = 0;

        for(int j = 0; j < N; j++){
            for(int k = M; k >= 0; k--){
                if(k >= seq[j]){
                    dp[k] = Math.max(dp[k], dp[k-seq[j]]+1);
                    //System.out.print(dp[k] + " ");
                }
            }
        }


        int ans = dp[M];
        if(ans <= 0){
            System.out.println("No");
        } else {
            System.out.println("Yes");
        }
    }
}