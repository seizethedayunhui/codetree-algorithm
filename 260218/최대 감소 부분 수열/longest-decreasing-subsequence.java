import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        int[] dp = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
            dp[i] = 1;
        }

        int ans = Integer.MIN_VALUE;

        for(int j = 0; j < N; j++){
            for(int k = 0; k < j; k++){
                if(arr[j] < arr[k]){
                    dp[j] = Math.max(dp[j], dp[k]+1);
                }
            }
            ans = Math.max(ans, dp[j]);
        }

        System.out.println(ans);
        
        
    }
}