import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int T = sc.nextInt();

        int[][] mat = new int[3][N];
        // 삼각형 왼쪽 위 변 -> 오른쪽 위 -> 맨 아래 쪽
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < N; j++ ){
                mat[i][j] = sc.nextInt();
            }
        }

        for(int i = 0; i < T; i++){

            int[] temps = {mat[0][N-1], mat[1][N-1], mat[2][N-1]};

            for(int j = 0; j < 3; j++){
                int temp = mat[j][N-1];
                for(int k = N-1; k > 0; k--){
                    mat[j][k] = mat[j][k-1];
                }
            }

            mat[0][0] = temps[2];
            mat[1][0] = temps[0];
            mat[2][0] = temps[1];
        }

        for(int row = 0; row < 3; row++){
            for(int col = 0; col < N; col++){
                System.out.print(mat[row][col] + " ");
            }
            System.out.println();
        }

    }
}