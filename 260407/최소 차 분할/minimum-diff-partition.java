import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }
        // 두개의 그룹으로 나누었을 때 그 그룹의 차이가 min이 되어야 함.

        // 만들 수 있는 최대합 구하기
        int m = 0;
        for(int e : arr){
            m += e;
        }

        boolean[][] dp = new boolean[n+1][m+1];

        dp[0][0] = true;

        for(int i = 1; i <= n; i++){
            for(int j = 0; j <= m; j++){
                // arr의 i번째 값까지 고려했을 때, j를 만들 수 있느냐?

                // 현재 값을 포함해서 만들 수 있는 경우
                if( j >= arr[i] && dp[i-1][j-arr[i]]){
                    dp[i][j] = true;
                }
                // 현재 값을 포함하지 않고 만들 수 있는 경우
                if (dp[i-1][j]){
                    dp[i][j] = true;
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < n+1; i++){
            for(int j = 0; j < m+1; j++){
                if (dp[i][j]){
                    int a = j;
                    int b = m-j;

                    answer = Math.min(answer, Math.abs(a-b));
                }
            }
        }

        System.out.println(answer);
        
    }
}