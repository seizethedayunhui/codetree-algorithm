import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();

        int[][] mat = new int[N][N];
        int[][] temp = new int[N][N];

        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int element = sc.nextInt();
                mat[i][j] = element;
                temp[i][j] = element;
            }
        }

        for(int k = 0; k < K; k++){
            for(int col = 0; col < N; col++){

                // 폭탄 처리 로직
                int startIdx = 0;
                int currentCnt = 0;
                int currentElement = mat[0][col];
                for(int row = 0; row < N; row++){

                    if (mat[row][col] == currentElement){
                        currentCnt += 1;
                    } else {
                        if (currentCnt >= M){
                            for (int l = startIdx; l < row; l++){
                                temp[l][col] = 0;
                            }
                        }

                        startIdx = row;
                        currentCnt = 1;
                        currentElement = mat[row][col];
                    }
                }

                if (currentCnt >= M){
                    for (int m = startIdx; m < N; m++){
                        temp[m][col] = 0;
                    }
                }
            }

            // 중력 처리 로직
            for(int c = 0; c < N; c++){
                for(int r = N-1; r > -1; r--){
                    if(temp[r][c] == 0){
                        for(int nextRow = r-1; nextRow > -1; nextRow--){
                            if (temp[nextRow][c]!=0){
                                temp[r][c] = temp[nextRow][c];
                                temp[nextRow][c] = 0;
                                break;
                            }
                        }
                    }
                }
            }

            // 복사 로직
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    mat[i][j] = temp[i][j];
                }
            }

            // for (int i = 0; i < N; i++){
            //     for(int j = 0; j < N; j++){
            //         System.out.print(mat[i][j] + " ");
            //     }
            //     System.out.println();
            // }

            // System.out.println();

            // 시계 방향 회전 로직
            for(int x = 0; x < N; x++){
                for(int y = 0; y < N; y++){
                    int nx = y;
                    int ny = N - x - 1;

                    temp[nx][ny] = mat[x][y];
                }
            }

            // 중력 처리 로직
            for(int c = 0; c < N; c++){
                for(int r = N-1; r > -1; r--){
                    if(temp[r][c] == 0){
                        for(int nextRow = r-1; nextRow > -1; nextRow--){
                            if (temp[nextRow][c]!=0){
                                temp[r][c] = temp[nextRow][c];
                                temp[nextRow][c] = 0;
                                break;
                            }
                        }
                    }
                }
            }

            // 복사 로직
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    mat[i][j] = temp[i][j];
                }
            }

            // 마지막 회전 후에도 폭발할 수 있으니 로직 추가
            for(int col = 0; col < N; col++){

                // 폭탄 처리 로직
                int startIdx = 0;
                int currentCnt = 0;
                int currentElement = mat[0][col];
                for(int row = 0; row < N; row++){

                    if (mat[row][col] == currentElement){
                        currentCnt += 1;
                    } else {
                        if (currentCnt >= M){
                            for (int l = startIdx; l < row; l++){
                                temp[l][col] = 0;
                            }
                        }

                        startIdx = row;
                        currentCnt = 1;
                        currentElement = mat[row][col];
                    }
                }

                if (currentCnt >= M){
                    for (int m = startIdx; m < N; m++){
                        temp[m][col] = 0;
                    }
                }
            }

            // for (int i = 0; i < N; i++){
            //     for(int j = 0; j < N; j++){
            //         System.out.print(mat[i][j] + " ");
            //     }
            //     System.out.println();
            // }

            // System.out.println();
        }

        // 복사 로직
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = temp[i][j];
            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(mat[i][j] != 0){
                    cnt += 1;
                }
            }
        }
        System.out.println(cnt);
    }
}