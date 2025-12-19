import java.util.*;

public class Main {

    public static int N;
    public static int[][] mat;

    public static boolean[] rows;
    public static boolean[] cols;

    public static int findMaxSum(int idx, int cnt, int currentSum){

        if (cnt == N){
            return currentSum; //합 계산 함수
        }

        if (idx == N || rows[idx]){
            return -1;
        }

        int maxSum = Integer.MIN_VALUE;

        rows[idx] = true;

            for(int j = 0; j < N; j++){

                if (cols[j] ){
                    continue;
                }

                cols[j] = true;
                maxSum = Math.max(maxSum, findMaxSum(idx+1, cnt + 1, currentSum + mat[idx][j]));
                cols[j] = false;
            }

        rows[idx] = false;

        return maxSum;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        mat = new int[N][N];
        rows = new boolean[N];
        cols = new boolean[N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        int ans = findMaxSum(0, 0, 0);
        System.out.println(ans);
    }
}