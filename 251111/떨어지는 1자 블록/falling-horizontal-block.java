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
        boolean findflag = false;
        int r = -1;

        for(int x = 0; x < N; x++){
            flag = true;

            for(int y = K; y < K + M; y++){
                if (mat[x][y] != 0){
                    flag = false;
                    findflag = true;
                    break;
                }
            }

            if (flag){
                r = x;
            }

            if (findflag){
                break;
            }
        }
        // flag가 true인 경우에 row 행을 1로 갱신 해줌
        for(int k = K; k < K + M; k++){
            mat[r][k] = 1;
        }

        for (int row = 0; row < N; row++){
            for(int col = 0; col < N; col++){
                System.out.print(mat[row][col]+ " ");
            }
            System.out.println();
        }


    }
}
