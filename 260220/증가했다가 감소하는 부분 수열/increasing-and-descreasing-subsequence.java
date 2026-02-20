import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        int[] upDp = new int[N];
        int[] dnDp = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
            upDp[i] = 1;
            dnDp[i] = 1;
        } 

        for(int i = 0; i < N; i++){
            for(int j = 0; j < i; j++){
                if (arr[i] > arr[j]){
                    upDp[i] = Math.max(upDp[i], upDp[j] + 1);
                }
            }
        }

        for(int i = N-1; i >= 0; i--){
            for(int j = N-1; j > i; j--){
                if(arr[i] > arr[j]){
                    dnDp[i] = Math.max(dnDp[i], dnDp[j] + 1);
                }
            }
        }

        int[] dp = new int[N];
        int ans = Integer.MIN_VALUE;

        for(int k = 0; k < N; k++){
            dp[k] = upDp[k] + dnDp[k];
            ans = Math.max(ans, dp[k]);
        }

        ans -=1;
        System.out.println(ans);
    }
}