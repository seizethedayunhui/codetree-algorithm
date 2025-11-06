import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] mat = new int[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        int r = sc.nextInt();
        int c = sc.nextInt();

        int x = r - 1;
        int y = c - 1;

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int nx;
        int ny;

        for(int i = 0; i < mat[x][y] - 1; i++){
            for(int j = 0; j < 4; j++){
                    nx = x + dx[j] * (i+1);
                    ny = y + dy[j] * (i+1);
                if ( nx >= 0 && nx < N && ny >= 0 && ny < N){
                        mat[nx][ny] = 0;
                }
            }
        }
        mat[x][y] = 0;


        int[][] temp = new int[N][N];

        for (int col = 0; col < N; col++){
            int k = N-1;
            for(int row = N-1; row > -1; row--){
                if (mat[row][col] != 0) {
                    temp[k][col] = mat[row][col];
                    k--;
                } 
            }
        }

        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = temp[i][j];
            }
        }

        for(int row = 0; row < N; row++){
            for(int col = 0; col < N; col++){
                System.out.print(mat[row][col] + " ");
            }
            System.out.println();
        }

    }
}