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

        boolean flag;
        for(int x = N-1; x > -1; x--){
            flag = true;
            for(int y = K; y < K + M; y++){
                if (mat[x][y] != 0){
                    flag = false;
                    break;
                }
            }

            if (flag){
                for(int y = K; y < K + M; y++){
                    mat[x][y] = 1;
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
