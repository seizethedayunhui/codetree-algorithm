import java.util.*;

public class Main {

    public static int N;
    public static int[][] mat;

    public static ArrayList<Integer> arr = new ArrayList<>();
    public static boolean[] rows;
    public static boolean[] cols;

    public static int calcSum(){

        int currentSum = 0;
        for(int i = 0; i < N; i++){
            currentSum += arr.get(i);
        }

        return currentSum;
    }

    public static int findMaxSum(){

        if (arr.size() == N){
            return calcSum(); //합 계산 함수
        }

        int maxSum = Integer.MIN_VALUE;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){

                if (rows[i] || cols[j] ){
                    continue;
                }

                arr.add(mat[i][j]);
                rows[i] = true;
                cols[j] = true;

                maxSum = Math.max(maxSum, findMaxSum());

                arr.remove(arr.size()-1);
                rows[i] = false;
                cols[j] = false;

            }
        }

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

        int ans = findMaxSum();
        System.out.println(ans);
    }
}