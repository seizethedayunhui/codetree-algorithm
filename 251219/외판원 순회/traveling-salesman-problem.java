import java.util.*;
public class Main {

    public static int N;
    public static int[][] mat;
    public static boolean[] visited;

    // start -> 0으로 두면됨
    public static int findMinSum(int currentSum, int location, int cnt){
        
        if (cnt == N-1){
            // System.out.println("들어옴");
            return currentSum + mat[location][0];
        }

        int minSum = Integer.MAX_VALUE;

        for(int i = 1; i < N; i++){

            if(visited[i]){
                continue;
            }

            visited[i] = true;
            minSum = Math.min(minSum, findMinSum(currentSum + mat[location][i], i, cnt+1));
            visited[i] = false;
        }

        return minSum;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        mat = new int[N][N];
        visited = new boolean[N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        int ans = findMinSum(0, 0, 0);

        System.out.println(ans);
    }
}