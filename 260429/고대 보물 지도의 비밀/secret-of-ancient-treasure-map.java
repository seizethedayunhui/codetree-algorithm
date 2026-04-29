import java.util.Scanner;

public class Main {
    public static int MIN_V = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            arr[i] = sc.nextInt();
        }

        // dp[i][j]: The maximum contiguous sum ending at index i using exactly j negative numbers
        int[][] dp = new int[N + 1][K + 1];
        for (int i = 0; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                dp[i][j] = MIN_V;
            }
        }

        for (int i = 1; i < N + 1; i++) {
            // Case 1: Current element is non-negative
            if (arr[i] >= 0) {
                // For j=0, decide whether to start a new subarray or continue from the previous one
                dp[i][0] = Math.max(arr[i], (dp[i - 1][0] == MIN_V) ? MIN_V : dp[i - 1][0] + arr[i]);

                for (int j = 1; j < K + 1; j++) {
                    // For j>0, continue from the previous state where j negative numbers were already used
                    if (dp[i - 1][j] != MIN_V) {
                        dp[i][j] = dp[i - 1][j] + arr[i];
                    }
                }
            } 
            // Case 2: Current element is negative
            else {
                for (int j = 1; j < K + 1; j++) {
                    // Transition from a state with j-1 negative numbers to include the current one
                    if (dp[i - 1][j - 1] != MIN_V) {
                        dp[i][j] = dp[i - 1][j - 1] + arr[i];
                    }
                }
                // Allow starting a new subarray with a single negative number (if K >= 1)
                if (K >= 1) {
                    dp[i][1] = Math.max(dp[i][1], arr[i]);
                }
            }
        }

        // Find the overall maximum value in the DP table
        int ans = MIN_V;
        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                if (dp[i][j] > ans) {
                    ans = dp[i][j];
                }
            }
        }
        System.out.println(ans);
    }
}