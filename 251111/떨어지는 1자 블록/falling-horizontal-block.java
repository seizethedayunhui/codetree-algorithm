import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        K--;

        int[][] mat = new int[N][N];
        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        boolean flag = false;
        for(int x = 0; x < N; x++){
            for(int y = K; y < K + M; y++){
                if (mat[x][y] == 1){
                    flag = true;
                    break;
                }
            }

            if (flag){
                for(int y = K; y < K + M; y++){
                    mat[x-1][y] = 1;
                }
                
                break;
            }
        }

        for (int row = 0; row < N; row++){
            for(int col = 0; col < N; col++){
                System.out.print(mat[row][col]+ " ");
            }
            System.out.println();
        }


    }
}